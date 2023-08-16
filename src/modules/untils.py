import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


def clean_text(lyric):
    n_lyric = re.sub('\d+',' ',n_lyric)
    n_lyric = re.sub('#',' ',n_lyric)
    n_lyric = n_lyric.lower()

    return n_lyric


def stemm_comments(words):
    words = words.split()
    stemmed_comment = []

    ps = PorterStemmer()
    
    for word in words:
        stemmed_word = ps.stem(word)
        stemmed_comment.append(stemmed_word)

    stemmed_comment = ' '.join(stemmed_comment)

    return stemmed_comment