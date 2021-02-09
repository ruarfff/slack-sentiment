from flask import Flask
from flask import request
import pickle
import nltk
from nltk import download
from nltk.tokenize import word_tokenize, sent_tokenize
import itertools


app = Flask(__name__)

model_file = open('sentiment_classifier.pickle', 'rb')
model = pickle.load(model_file)
model_file.close()

download('stopwords')
download('names')
download('punkt')

from nltk.corpus import stopwords, names
from string import punctuation

name_words = set([n.lower() for n in names.words()])
stop_words = set(stopwords.words("english"))

def clean_words(words):
    return [w for w in [w.lower() for w in words if w.isalpha()] if w not in stop_words and w not in name_words and w not in punctuation]

def word_counts(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


@app.route('/', methods=['GET', 'POST'])
def classify_text():
    if request.method == 'POST':
        text = request.form.get('text')
        tokenized_text = [sent_tokenize(t) for t in text]
        sentences = list(itertools.chain(*tokenized_text))
        tokenized_words = [word_tokenize(sentence) for sentence in sentences]
        words = clean_words(list(itertools.chain(*tokenized_words)))

        res = model.classify(word_counts(words))

        if res == 'neg':
            return 'That text appears to be negative :('
        else:
            return 'That text appears to be positive :)'
    else:
        return 'You need to POST some data to test this endpoint'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
