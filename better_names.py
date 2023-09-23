import text
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

shandy = text.shandy

results = ne_chunk(pos_tag(word_tokenize(shandy)))

for result in results:
    if type(result) == Tree:
        name = ''
        for result_leaf in result.leaves():
            name += result_leaf[0] + ' '
        print ('Type: ', result.label(), 'Name: ', name)