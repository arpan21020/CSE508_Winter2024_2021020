import os
import pickle

directory_path = './Dataset'
file_list = os.listdir(directory_path)

def inverted_index():
    inverted_index = {}
    for filename in file_list:
        with open(directory_path + '/' + filename, 'r') as file:
            data = file.read()
            words = data.split()
            for word in words:
                if word not in inverted_index:
                    inverted_index[word] = [set(),0]
                inverted_index[word][0].add(filename)
                inverted_index[word][1]+=1
    return inverted_index

inverted_idx = inverted_index()
with open('unigram_inverted_index.dat', 'wb') as file:
    pickle.dump(inverted_idx, file)
    
# with open('unigram_inverted_index.dat', 'rb') as f:
#     loaded_unigram_index = pickle.load(f)

# print("Inverted Index:\n")
# for i in loaded_unigram_index:
#     print(i,loaded_unigram_index[i])