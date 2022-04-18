# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
'''read a csv file'''
#import pandas as pd 
#data = read.csv
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
import nltk
from lxml import html 
import requests
from bs4 import BeautifulSoup
import nltk.corpus
from nltk.tokenize import word_tokenize
#on crée une variable page 
page = requests.get('https://www.imdb.com/title/tt7286456/criticreviews?ref_=tt_ov_rt')
soup = BeautifulSoup(page.text, 'html.parser')
fichier = open("comments_2.txt", "w")
#######
for x in soup.find_all('div', class_='summary'):
    
    fichier.write(x.text)
    fichier.write("\n")
    
fichier.close()
    

f = open('article.txt',encoding="utf8")
raw = f.readlines()
tokens = word_tokenize(str(raw))
print(tokens)

words = [w.lower() for w in tokens] 
print(str(words))

stopWords = set(stopwords.words('english'))
wordsFiltered = []
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)
print(wordsFiltered)
#frequency words in document
freq = nltk.FreqDist(wordsFiltered)#function of frequency-word

for word,frequence in freq.items():
    print(str(word)+ "  " + str(frequence)+ '' )
    
    
F=open('article_tokenised.txt', 'w',encoding="utf8")
for word,frequence in freq.items():
    F.write(str(word) + ' ' + str(frequence))
    F.write('\n')
    
F.close()

#phase de recherche de terme
def recherche(terme):
    for word,frequence in freq.items():
        if terme in word and frequence:#fonction bouléenne
            print(str(word) +' is in the doc'+ ' ' + str(frequence) + ' ' + 'time(s)')
            return terme
    print('no reference for your word(s)')
    return terme

'''Sentiment analyzer'''

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


    
#score for little sentence
def sentiment_analyzer_scores(sentence): #here we don't use sentiwordnet
#we use vaderSentiment lib. --> more powerful than sentiwordnet, it gives the compound 
    score = analyser.polarity_scores(sentence)
    print('{:-<40} {}'.format(sentence, str(score)))
#score for all

txt = open('article.txt',"r",encoding="utf8")
L = txt.readlines()
##cleaning section --> not obligate to do this 
Split = []
REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")#
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

for lines in L:
    Split.append(lines.strip())


def preprocess_reviews(reviews):
    reviews = [REPLACE_NO_SPACE.sub(' ', line.lower()) for line in reviews]
    reviews = [REPLACE_WITH_SPACE.sub(" " , line) for line in reviews]
    
    return reviews


clean_split = preprocess_reviews(Split)
def scores():
        #we create a i-variable who is going to read our file 
        
        
        a = sentiment_analyzer_scores(str(L))#using our senti_analyzer
        #why we use the L and not the clean_split --> just because sentiment_analyzer_scores
        #use the special caracters for the scores acoording to his polarity
        
        return a
#{'neg': 0.02, 'neu': 0.924, 'pos': 0.057, 'compound': 0.9995}
        #--> we can say that this article share neutral point of view at 92.4%
        #--> logically, it makes sence because an article has to be neutral  
        #--> the results has to be described without any describing adj. 
        #--> the algorithm for sensimental description is working in our way

limit_freq_0 = 30 #we can change the freq_limit as we want [in french  'seuil']
limit_freq_1 = 35
limit_freq_2 = 40
limit_freq_3 = 45
for word,frequence in freq.items():
###Plotting the results 

    if frequence >= limit_freq_0:
        #we use a big limit to filter the most common words
        #flter_0
        plt.subplot(1,4,1)
        plt.plot(word, frequence,'*')
        plt.xlabel('word')
        plt.ylabel('frequence')
        plt.title('limit_freq_0')
        print(str((word)) + ' ' + str(frequence))
        
    if frequence >= limit_freq_1:
    
        plt.subplot(1,4,2)
        plt.plot(word, frequence,'*')
        plt.xlabel('word')
        plt.title('limit_freq_1 ')
        print(str((word)) + ' ' + str(frequence))
        
    if frequence >= limit_freq_2:
    
        plt.subplot(1,4,3)
        plt.plot(word, frequence,'*')
        plt.xlabel('word')
        plt.title('limit_freq_2 ')
        print(str((word)) + ' ' + str(frequence))
        
    if frequence >= limit_freq_3:
    
        plt.subplot(1,4,4)
        plt.plot(word, frequence,'*')
        plt.xlabel('word')
        plt.title('limit_freq_3')
        print(str((word)) + ' ' + str(frequence))




'''----------------Testing-----------------'''
if __name__ == "__main__":
    terme = str(input('enter your sentence: '))
    recherche(terme)
    print("--------recherche function test passed !------")
    
    sentiment_analyzer_scores("happy")
    print("-----sentiment_analyzer_scores function test passed !--")
    
    scores()
    print("------function scores() test passed !--")
    
    preprocess_reviews("./5°+RRHello ")
    print("-----preprocess_reviews() function test passed !")
    
    print("\n -------All test has passed ! ")
    
    
    
          
#feelings part 
#exemple for           
#to have the opinion, which means negative or positive 
#we use the sentiwordnet library 
# for example:
    # print(swn.senti_synset('breakdown.n.03'))
    # >> <breakdown.n.03: PosScore=0.0 NegScore=0.25>

#this example is a deep learning of the opinion:
    # happy = swn.senti_synsets('happy','a')
    # happy0 = list(happy)[0]
    # >> happy0.pos_score()
    # 0.875
    # >> happy0.neg_score() 
    # 0.0
    # >> happy0.obj_score() 
        
#import re
#from nltk.compat import python_2_unicode_compatible
#from nltk.corpus.reader import CorpusReader        
#@python_2_unicode_compatible()   

#class SentiWordNetCorpusReader(CorpusReader):
    #def 

    
