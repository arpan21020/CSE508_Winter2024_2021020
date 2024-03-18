import os
import pandas as pd
from textPreprocessing import TextPreprocessor 
from if_idf import TFIDFCalculator
import json
import pickle
def read_reviews_from_csv(csv_file):
    try:
        df = pd.read_csv(csv_file)
        
        third_column_values = df.iloc[:, 2].tolist()
        
        return third_column_values
    except Exception as e:
        print("An error occurred:", e)
        return None
def read_processed_reviews(directory):
    file_contents = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                file_contents.append(file.read())
    return file_contents

def text_features():
    csv_file = "A2_Data.csv"
    reviews = read_reviews_from_csv(csv_file)
    print("Reviews:",len(reviews))
    if not os.path.exists('./Reviews_Dataset'):
            os.makedirs('./Reviews_Dataset')
    # file=open('not_found_reviews.txt', 'w')
    # for i in range(1, len(reviews)+1):
    #     review=reviews[i-1]
    #     # print(i,review)
    #     if pd.isna(review):
    #         file.write("Row "+str(i+1)+" has empty review"+'\n')
    #         print("Row "+str(i+1)+" has empty review"+'\n')
    #         continue
    #     preprocessor = TextPreprocessor()
    #     preprocessed_review = preprocessor.preprocess_text(review)
    #     path="./Reviews_Dataset/review_{}.txt".format(i)
    #     with open(path,"w") as f:
    #         f.write(preprocessed_review)
        
    # file.close()
    reviews_documents=read_processed_reviews('./Reviews_Dataset')
    tfidf_calculator = TFIDFCalculator([doc.split() for doc in reviews_documents],len(reviews))
    similarity_scores = tfidf_calculator.calculate_all_cosine_similarity()
    with open("reviews_cosine_similarities.json","w") as f:
        json.dump(similarity_scores,f)
        
    with open("reviews_cosine_similarity.dat","wb") as f:
        pickle.dump(similarity_scores,f)
    
    

if __name__=="__main__":
    text_features()
    