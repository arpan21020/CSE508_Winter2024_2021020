import os
import pickle

directory_path = './Dataset'
file_list = os.listdir(directory_path)

def positional_index():
    positional_index = {}
    for filename in file_list:
        with open(directory_path + '/' + filename, 'r') as file:
            data = file.read()
            words = data.split()
            for pos in range(len(words)):
                
                if words[pos] not in positional_index:
                    positional_index[words[pos]] = [{},0]
                if filename not in positional_index[words[pos]][0]:
                    positional_index[words[pos]][0][filename] = []
                positional_index[words[pos]][0][filename].append(pos+1)
                positional_index[words[pos]][1]=len(positional_index[words[pos]][0])
    return positional_index
                
                

positional_idx = positional_index()
with open('positional_index.dat', 'wb') as file:
    pickle.dump(positional_idx, file)
    
# with open('positional_index.dat', 'rb') as f:
#     loaded_unigram_index = pickle.load(f)

# print("Positional Index:\n")
# for i in loaded_unigram_index:
#     print(i,loaded_unigram_index[i])