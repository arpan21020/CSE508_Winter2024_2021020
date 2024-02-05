import nltk
import string
# nltk.download('punkt')
# nltk.download('stopwords')

class DataPreprocessing:
    def __init__(self, data):
        self.data = data
    
    def lowercase(self):
        self.data.lower()
    
    def tokenization(self):
        self.data=nltk.tokenize.word_tokenize(self.data)
    def stop_word_removal(self):
        stop_words = set(nltk.corpus.stopwords.words('english'))
        self.data = [word for word in self.data if word not in stop_words]
    def remove_punctuation(self):
         self.data=self.data.translate(str.maketrans("", "", string.punctuation))
    
    def remove_blank_spaces(self):
        self.data= ' '.join(self.data)
        
    
    def process_all(self):
        self.remove_punctuation()
        self.lowercase()
        self.tokenization()
        self.stop_word_removal()
        self.remove_blank_spaces() 
        
        
    
    
    
    
    
