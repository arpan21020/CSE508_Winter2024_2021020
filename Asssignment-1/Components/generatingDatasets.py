import os
from .data_preprocessing import DataPreprocessing

def datasetGen():
        directory_path = './text_files'
        if not os.path.exists('./Dataset'):
            os.makedirs('./Dataset')
        file_list = os.listdir(directory_path)

        for filename in file_list:
            with open(directory_path + '/' + filename, 'r') as file:
                data = file.read()
                dataset=DataPreprocessing(data)
                dataset.process_all()
            with open('./Dataset/' + filename, 'w') as file:
                file.write(dataset.data)
    
        print("Dataset Generated")
