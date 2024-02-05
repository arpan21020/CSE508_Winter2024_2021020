
import pickle
from .data_preprocessing import DataPreprocessing


with open ('unigram_inverted_index.dat', 'rb') as f:
    inverted_index = pickle.load(f)

universal_set = set()
for docs in inverted_index.values():
    universal_set = universal_set.union(docs[0])


class BooleanQueries:
    def __init__(self, query,operations):
        self.query = query  #string
        self.operations=operations #list of operations
        
    @staticmethod
    def and_operation(set1, set2):
        return set1.intersection(set2)
    
    @staticmethod
    def or_operation(set1, set2):
        return set1.union(set2)
    
    @staticmethod
    def and_not_operation(set1, set2):
        return set1.difference(set2)
    
    @staticmethod
    def or_not_operation(set1, set2):
        complement_set2 = universal_set - set2
        return set1.union(complement_set2)
    
    
    def query_form(self):
        obj=DataPreprocessing(self.query)
        obj.process_all()
        query=obj.data.split()
        query_x=[]
        query_x.append(query[0])
        for i in range(1,len(query)):
            query_x.append(self.operations[i-1])
            query_x.append(query[i])
        return ' '.join(query_x)
        
    def processing_operations(self):
        obj=DataPreprocessing(self.query)
        obj.process_all()
        query=obj.data.split()
        
        result=inverted_index[query[0]][0]
        for i in range(1,len(query)):
            key=query[i]
            
            if self.operations[i-1]=='AND':
                result=self.and_operation(result,inverted_index[key][0]) 
            elif self.operations[i-1]=='OR':
                result=self.or_operation(result,inverted_index[key][0])
            elif self.operations[i-1]=='OR NOT':
                result=self.or_not_operation(result,inverted_index[key][0])
            elif self.operations[i-1]=='AND NOT':
                result=self.and_not_operation(result,inverted_index[key][0])
        return result
    


# onj=BooleanQueries("Loving these vintage? springs!",['AND','OR'])
# res=onj.processing_operations()
# print(res)