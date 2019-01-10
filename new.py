# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:50:31 2017

@author: Ali Asghar Marvi
"""

import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from collections import Counter
#
from Unsupervised import Unsupervised
STOPWORDS = set(stopwords.words('english'))
df = pd.read_csv('reviews_reduced.csv', encoding='latin-1')

corpus = []
#noun_counter = Counter()
#

model = Unsupervised()
#tokenize = word_tokenize()
def score(sentence):
    sentence = word_tokenize(sentence)
    score = model.predict(sentence)
    return score

def aspects(sentences):
    noun_counter = Counter()
    for sent in sentences:  
        for word,pos in sent:
            if pos=='NNP' or pos=='NN' and word not in STOPWORDS:
                noun_counter[word] += 1
    return [noun for noun, _ in noun_counter.most_common(15)]

array = []
def tokens_to_string(array):
    sentence = ' '.join(map(str, array))
#    sentence = "" + (word for word in array) + " "
    return sentence
for i in range(len(df)):
    review = re.sub('[^a-zA-Z0-9]', ' ', df['Text'][i])
    review = review.lower()
    corpus.append(review)

for i in range(len(corpus)):
    corpus[i] = [word_tokenize(corpus[i])]   
#    corpus[i] = [word for word in corpus[i]]
    corpus[i] = [nltk.pos_tag(word) for word in corpus[i]]
    corpus[i] = aspects(corpus[i])
    corpus[i] = tokens_to_string(corpus[i])
    print(str(i+1) + " "+corpus[i])
    print(score(corpus[i]))

#print(corpus[0])


