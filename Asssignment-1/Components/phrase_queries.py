import pickle

from .data_preprocessing import DataPreprocessing


with open ('positional_index.dat', 'rb') as f:
    positional_index = pickle.load(f)

class PhraseQueries:
    def __init__(self, query):
        self.query = query
    
    def processing_query(self):
        obj=DataPreprocessing(self.query)
        obj.process_all()
        query=obj.data.split()
        if(query[0] in positional_index.keys()):
            resulting_docs=set(positional_index[query[0]][0].keys())
        else:
            resulting_docs=set()
        for i in range(1,len(query)):
            key=query[i]
            if(key in positional_index.keys()):
                resulting_docs=resulting_docs.intersection(set(positional_index[key][0].keys()))
            else:
                resulting_docs=set()
        output_files=[]
        if(len(resulting_docs)==0):
            return output_files
        for doc in resulting_docs:
            positions=positional_index[query[0]][0][doc]
            bit=[0]*len(query)
            bit[0]=1
            for pos in positions:
                for i in range(1,len(query)):
                    if (pos+i in positional_index[query[i]][0][doc]):
                        bit[i]=1
            if(0 not in bit):
                output_files.append(doc)
        return output_files       
