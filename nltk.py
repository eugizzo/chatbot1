import nltk

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
import numpy as np

sentence='hello there this nlp '
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

print(tokenize(sentence))

word_stemmer="'good','goodmorning','gooder'"

www= stem[stem(w),w in word_stemmer]

print(www)