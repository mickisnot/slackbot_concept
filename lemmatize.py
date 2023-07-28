import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def lemma(message):
    words = word_tokenize(message)
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words


