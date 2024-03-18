import math
from collections import Counter

class TFIDFCalculator:
    def __init__(self, documents,num_documents):
        self.documents = documents
        self.n=num_documents
        self.tf_idf_scores = []

    def calculate_tf_idf(self, document):
        tf = Counter(document)
        total_words = len(document)
        tf = {word: tf[word] / total_words for word in tf}
        idf = {}
        for word in tf:
            num_documents_with_word = sum(1 for doc in self.documents if word in doc)
            idf[word] = math.log(self.n / (1 + num_documents_with_word),10)

        tf_idf = {word: tf[word]* idf[word] for word in tf}
        return tf_idf

    def cosine_similarity(self, doc1, doc2):
        tfidf_doc1 = self.calculate_tf_idf(doc1)
        tfidf_doc2 = self.calculate_tf_idf(doc2)

        dot_product = sum(tfidf_doc1.get(word, 0) * tfidf_doc2.get(word, 0) for word in set(tfidf_doc1) & set(tfidf_doc2))
        magnitude_doc1 = math.sqrt(sum(value ** 2 for value in tfidf_doc1.values()))
        magnitude_doc2 = math.sqrt(sum(value ** 2 for value in tfidf_doc2.values()))

        if magnitude_doc1 != 0 and magnitude_doc2 != 0:
            cosine_similarity = dot_product / (magnitude_doc1 * magnitude_doc2)
        else:
            cosine_similarity = 0

        return cosine_similarity
    
    def calculate_all_cosine_similarity(self):
        all_cosine_similarity = {}
        # i+2 and j+2 contains the row number of the review in the csv file 
        for i in range(len(self.documents)):
            all_cosine_similarity[i] = {}
        for i in range(len(self.documents)):
            for j in range(i+1,len(self.documents)):
                if i == j:
                    continue
                similarity = self.cosine_similarity(self.documents[i], self.documents[j])
                all_cosine_similarity[i][j]=similarity
                all_cosine_similarity[j][i]=similarity
                
            print(f"Row :{i+2} done...")
        return all_cosine_similarity

# # Example usage:
# documents = [
#     "The quick brown fox jumps over the lazy dog.",
#     "Dogs are friendly animals.",
#     "Cats and dogs are pets."
# ]

# tfidf_calculator = TFIDFCalculator([doc.split() for doc in documents])
# tfidf_scores = tfidf_calculator.calculate_all_tf_idf()

# # Print TF-IDF scores for each document
# for i, tfidf_score in enumerate(tfidf_scores):
#     print(f"TF-IDF scores for document {i+1}: {tfidf_score}")
