import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('names')
from nltk import word_tokenize, pos_tag
from nltk.corpus import names
import text

shandy_text = text.shandy

names = set(names.words())

tokens = word_tokenize(shandy_text)

tagging = pos_tag(tokens)

proper_nouns = [word for word, pos in tagging if pos in ['NNP', 'NNPS'] and word in names]

print(proper_nouns)