import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

class TextPreprocessor:
    def __init__(self):
        # nltk.download('punkt')
        # nltk.download('stopwords')
        # nltk.download('wordnet')
        pass

    def lower_case(self, text):
        return text.lower()

    def tokenize(self, text):
        return word_tokenize(text)

    def remove_punctuation(self, tokens):
        return [token for token in tokens if token not in string.punctuation]

    def remove_stopwords(self, tokens):
        stop_words = set(stopwords.words('english'))
        return [token for token in tokens if token not in stop_words]

    def stem(self, tokens):
        stemmer = PorterStemmer()
        return [stemmer.stem(token) for token in tokens]

    def lemmatize(self, tokens):
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(token) for token in tokens]

    def preprocess_text(self, text):
        text = self.lower_case(text)
        tokens = self.tokenize(text)
        tokens = self.remove_punctuation(tokens)
        tokens = self.remove_stopwords(tokens)
        tokens = self.stem(tokens)
        tokens = self.lemmatize(tokens)
        return ' '.join(tokens)


