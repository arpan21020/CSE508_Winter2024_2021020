import os
from data_preprocessing import DataPreprocessing
directory_path = './text_files'


# Get a list of all files in the directory
file_list = os.listdir(directory_path)

for filename in file_list:
    with open(directory_path + '/' + filename, 'r') as file:
        data = file.read()
        dataset=DataPreprocessing(data)
        dataset.process_all()
    with open('./Dataset/' + filename, 'w') as file:
        file.write(dataset.data)
    