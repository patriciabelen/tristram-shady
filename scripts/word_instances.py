import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import text

nltk.download('stopwords')
nltk.download('punkt')

shandy = text.shandy

words = word_tokenize(shandy.lower())
filtered_words = [word for word in words 
                  if word.isalnum() and word not in stopwords.words('english')]

words_counts = Counter(filtered_words)
sorted_word_counts = dict(words_counts.most_common())

for word, count in sorted_word_counts.items():
    print(f'{word}: {count}')