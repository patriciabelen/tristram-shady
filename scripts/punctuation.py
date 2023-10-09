import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import string
import text 
import time

text = text.shandy

tokens = word_tokenize(text)
punctuation_tokens = [token for token in tokens if token in string.punctuation]

# print(punctuation_tokens)

for punct in punctuation_tokens:
    for char in punct:
        print(char, end='', flush=True)
        time.sleep(0.01)  