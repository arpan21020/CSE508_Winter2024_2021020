from keras.applications import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
from sklearn.preprocessing import StandardScaler
import pickle
import json
import numpy as np
import os

class ResNetFeatureExtractor:
    def __init__(self):
        self.model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

    def extract_features(self, image_path):
        img = image.load_img(image_path)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        features = self.model.predict(x)
        return features
    def cosine_similarity(self, vector1, vector2):
        vector1 = np.array(vector1).reshape(-1)
        vector2 = np.array(vector2).reshape(-1)
        dot_product = np.dot(vector1, vector2)
        norm_a = np.linalg.norm(vector1)
        norm_b = np.linalg.norm(vector2)
        return dot_product / (norm_a * norm_b)
if __name__=="__main__":
    # Example usage:
    training_set_path = "./Image_Dataset/"
    feature_extractor = ResNetFeatureExtractor()

    # Iterate through images in the training set directory
    i=0
    scaler = StandardScaler()
    filenames = []
    extracted_features={}
    for filename in os.listdir(training_set_path):
        if filename.endswith(".jpg"):
            image_path = os.path.join(training_set_path, filename)
            features = feature_extractor.extract_features(image_path)
            normalized_features = scaler.fit_transform(features.reshape(-1,1))
            filename = os.path.splitext(filename)[0]
            extracted_features[filename]=normalized_features.tolist()
            filenames.append(filename)
    with open("extracted_features.dat", "wb") as file:
        pickle.dump(extracted_features, file)
    with open("image_extracted_feature.json", "w") as file:
        json.dump(extracted_features, file) 
   
    # # [file1:{file2:cosine_similarity}]
    with open("extracted_features.dat", "rb") as file:
        extracted_features = pickle.load(file)
    images_cosine_similarity = {}
    for file1 in extracted_features.keys():
        images_cosine_similarity[file1]={}
        for file2 in extracted_features.keys():
            if file1 != file2:
                similarity = feature_extractor.cosine_similarity(extracted_features[file1], extracted_features[file2])
                images_cosine_similarity[file1][file2]=similarity
                
    with open("images_cosine_similarity.dat", "wb") as file:
        pickle.dump(images_cosine_similarity, file)