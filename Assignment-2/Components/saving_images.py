import pandas as pd
from imagePreprocessing import ImageProcessor
import os
import ast
import json
def read_image_urls_from_csv(csv_file):
    try:
        df = pd.read_csv(csv_file)
        
        image_urls = []
        for urls_list in df.iloc[:, 1]:
            urls = ast.literal_eval(urls_list)  # Convert string representation of list to actual list
            image_urls.append(urls)
        filename_to_url_map={}
        filename_to_index_map={}
        prefix="file"
        i=1
        row=0
        for url_lists in image_urls:
            for url in url_lists:
                filename=prefix+str(i)+".jpg"
                filename_to_url_map[url]=filename
                if(row>=830):
                    filename_to_index_map[prefix+str(i)]=row-1
                    
                else:
                    filename_to_index_map[prefix+str(i)]=row
                i+=1
            row+=1
        with open('filename_to_url_map.json', 'w') as json_file:
            json.dump(filename_to_url_map, json_file)
        with open('filename_to_index_map.json', 'w') as json_file:
            json.dump(filename_to_index_map, json_file)
                
        return image_urls
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

# Example usage:
if __name__ == "__main__":
    csv_file = "A2_Data.csv"
    image_urls = read_image_urls_from_csv(csv_file)
    print("Image URLs:",len(image_urls))
    if not os.path.exists('./Image_Dataset'):
            os.makedirs('./Image_Dataset')
    file=open("not_found_urls.txt","w")
    row=2
    for url_list in image_urls:    
        for url in url_list:
            # print(url)
            image_processor = ImageProcessor(url)
            if(image_processor.url_not_found):
                file.write("Row:"+str(row)+"  URL:"+url+"\n")
                continue
            image_processor.processing_image()
        row+=1
    file.close()
