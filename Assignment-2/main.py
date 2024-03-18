import signal
import sys
import json
import pickle
import pandas as pd
import numpy as np
import ast


def signal_handler(sig, frame):
    
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


with open("filename_to_url_map.json", 'r') as file:
    filename_to_url_map = json.load(file)
with open("filename_to_index_map.json", "r") as file:
    filename_to_index_map=json.load(file)
with open("images_cosine_similarity.dat", "rb") as file:
    images_cosine_similarity = pickle.load(file)
with open("reviews_cosine_similarity.dat", "rb") as file:
    reviews_cosine_similarity = pickle.load(file)

   

# for key in images_cosine_similarity.keys():
#     my_dict=images_cosine_similarity[key]
#     my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
#     images_cosine_similarity[key]=my_dict


# with open("sorted_image_cosines.json","w") as file:
#             json.dump(images_cosine_similarity,file)
    
# for key in reviews_cosine_similarity.keys():
#     my_dict=reviews_cosine_similarity[key]
#     my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
#     reviews_cosine_similarity[key]=my_dict

# with open("sorted_review_cosines.json","w") as file:
#     json.dump(reviews_cosine_similarity,file)
    
    



def read_image_urls_from_csv(csv_file):
        composite_similarity={}

        df = pd.read_csv(csv_file)
        
        i=0
        for urls_list in df.iloc[:, 1]:
            urls = ast.literal_eval(urls_list)  # Convert string representation of list to actual list
            for url in urls:
                filename=filename_to_url_map[url]
                filename=filename.split(".")[0]

                composite_similarity[str((filename,filename_to_index_map[filename]))]={}
                for key in images_cosine_similarity[filename]:
                    img_similarity=images_cosine_similarity[filename][key]
                    # print(filename,key)
                    if(filename_to_index_map[filename]==filename_to_index_map[key]):
                        text_similarity=1
                    else:
                        text_similarity=reviews_cosine_similarity[str(filename_to_index_map[filename])][str(filename_to_index_map[key])]    
                    avg_similarity=(img_similarity+text_similarity)/2
                    composite_similarity[str((filename,filename_to_index_map[filename]))][str((key,filename_to_index_map[key]))]=avg_similarity
                    
                
                if(i>2):
                    break
                i+=1
        with open("composite_similarity.json","w") as file:
            json.dump(composite_similarity,file)
                
# read_image_urls_from_csv("A2_Data.csv")
  

with open("composite_similarity.json","r") as file:
    composite_similarity=json.load(file)
    
for key in composite_similarity:
    my_dict=composite_similarity[key]
    my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    composite_similarity[key]=my_dict
with open("sorted_composite_similarity.json","w") as file:
    json.dump(composite_similarity,file)    

##################### Reading the sorted files according to similarity############################

with open("sorted_image_cosines.json","r") as file:
    sorted_images_cosine_similarity=json.load(file)
with open("sorted_review_cosines.json","r") as file:
    sorted_reviews_cosine_similarity=json.load(file)
with open("sorted_composite_similarity.json","r") as file:
    sorted_composite_similarity=json.load(file)

def find_url(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None




def part4():
    print("*"*40)
    print("\033[1m Image and Text Query Input : \033[0m")
    img_input="https://images-na.ssl-images-amazon.com/images/I/81q5+IxFVUL._SY88.jpg"
    review_input="Loving these vintage springs on my vintage strat. They have a good tension and great stability. If you are floating your bridge and want the most out of your springs than these are the way to go."
    
    filename=filename_to_url_map[img_input]
    filename=filename.split(".")[0]
    value_to_search = review_input
    column_to_search = 'Review Text'
    k=3
    df = pd.read_csv('A2_Data.csv')
    matching_rows = np.where(df[column_to_search] == value_to_search)[0][0]
    print("\033[1m USING COMPOSITE SIMILARITY \033[0m")
    for i,key in enumerate(sorted_composite_similarity[str((filename,filename_to_index_map[filename]))]):
        if i==k:
            break
        f=ast.literal_eval(key)[0]
        corresponding_review_row=ast.literal_eval(key)[1]
        print("\033[1m Image Url : \033[0m",find_url(filename_to_url_map,f+".jpg"))
        print("\033[1m Review : \033[0m",df.loc[filename_to_index_map[f],column_to_search]) 
        print("\033[1m Cosine similarity of images : \033[0m",sorted_images_cosine_similarity[filename][f]) 
        print("\033[1m Cosine similarity of text : \033[0m",sorted_reviews_cosine_similarity[str(matching_rows)][str(corresponding_review_row)])
        print("\033[1m Composite similarity : \033[0m",sorted_composite_similarity[str((filename,filename_to_index_map[filename]))][str((f,corresponding_review_row))])   
        print()
part4()
while True:
    print("*"*40)
    print("Press Ctrl+C for exit....")
    print("\033[1m Image and Text Query Input : \033[0m")
    img_input=input("Image : ")
    review_input=input("Review : ")
    
    filename=filename_to_url_map[img_input]
    filename=filename.split(".")[0]
    
    df = pd.read_csv('A2_Data.csv')

# Search for an element in the DataFrame
# For example, let's say you want to search for a specific value in a specific column
    value_to_search = review_input
    column_to_search = 'Review Text'

   
    # You can also get the rows where the value exists
    matching_rows = np.where(df[column_to_search] == value_to_search)[0][0]
    print(filename)
    print(matching_rows)
    
    
    row=str(matching_rows+2)
    
  
    print("*"*40)
    print("\033[1m USING IMAGE RETRIEVAL \033[0m")
    # print("\033[1m Top 3 Similar Images : \033[0m")
    
    k = 3

    for i, key in enumerate(sorted_images_cosine_similarity[filename]):
        if i == k:
            break        
        print("\033[1m Image Url : \033[0m",find_url(filename_to_url_map,key+".jpg"))
        corresponding_review_row=filename_to_index_map[key]
        print("\033[1m Review : \033[0m",df.loc[corresponding_review_row,column_to_search])
        print("\033[1m Cosine similarity of images : \033[0m",sorted_images_cosine_similarity[filename][key]) 
        print("\033[1m Cosine similarity of text : \033[0m",sorted_reviews_cosine_similarity[str(matching_rows)][str(corresponding_review_row)])
        print("\033[1m Composite similarity : \033[0m",sorted_composite_similarity[str((filename,filename_to_index_map[filename]))][str((key,corresponding_review_row))])   
        print()
    print("*"*40)
    print("\033[1m USING TEXT RETRIEVAL \033[0m")
    for i,key in enumerate(sorted_reviews_cosine_similarity[str(matching_rows)]):
        if i==k:
            break
        url=ast.literal_eval(df.loc[int(key), 'Image'])
        print("\033[1m Image Url : \033[0m",url)
        image=filename_to_url_map[url[0]]
        image=image.split(".")[0]
        corresponding_review_row=filename_to_index_map[image]
        
        print("\033[1m Review : \033[0m",df.loc[corresponding_review_row,column_to_search])
        print("\033[1m Cosine similarity of images : \033[0m",[sorted_images_cosine_similarity[filename][filename_to_url_map[img].split(".")[0]] for img in url]) 
        print("\033[1m Cosine similarity of text : \033[0m",sorted_reviews_cosine_similarity[str(matching_rows)][str(corresponding_review_row)])
        print("\033[1m Composite similarity : \033[0m",[sorted_composite_similarity[str((filename,filename_to_index_map[filename]))][str((filename_to_url_map[img].split(".")[0],corresponding_review_row))] for img in url])   
        print()
    print("*"*40)
   
        
        
    
 