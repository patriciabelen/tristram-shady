import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import string
import text 

text = text.text 

tokens = word_tokenize(text)
punctuation_tokens = [token for token in tokens if token in string.punctuation]

print(punctuation_tokens)