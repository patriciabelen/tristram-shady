import text
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

shandy = text.shandy

nltk_results = ne_chunk(pos_tag(word_tokenize(shandy)))
for nltk_result in nltk_results:
    if type(nltk_result) == Tree:
        name = ''
        for nltk_result_leaf in nltk_result.leaves():
            name += nltk_result_leaf[0] + ' '
        print ('Type: ', nltk_result.label(), 'Name: ', name)