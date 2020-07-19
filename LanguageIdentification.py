#!/usr/bin/env python
# coding: utf-8

# In[65]:


# Author: Sara Mesbahi & El-hassouni Fatima-Zahrae
# Purpose: Example for detecting language using a stopwords based approach
# Created: 15/07/2020

import sys

try:
    from nltk import wordpunct_tokenize
    from nltk.corpus import stopwords
except ImportError:
    print ("[!] You need to install nltk (http://nltk.org/index.html)")

def _calc_ratios(text):

    """
    Calculate probability of given text to be written in several languages and
    return a dictionary that looks like {'french': 2, 'spanish': 4, 'english': 0}
    """
    ratios = {}

    #nltk.wordpunct_tokenize() splits all punctuations into separate tokens
    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]
    

    # Compute per language included in nltk number of unique stopwords appearing in analyzed text
    for lang in stopwords.fileids():
        stopwords_set = set(stopwords.words(lang))
        words_set = set(words)
        common_words = words_set.intersection(stopwords_set)

        ratios[lang] = len(common_words) #language score

    return ratios

def _calc_probability(most, secode_most) :
    
    """
    Calculate probability of given text to be written in several languages and
    return the highest scored.
    
    It uses a stopwords based approach, counting how many unique stopwords
    are seen in analyzed text.
    """
    
    proba = (float(most) /(most + secode_most) * 100)
    return round(proba)

def _calc_words(text) :
    """
    If we suppose that our text is containing different languages, 
    this function is to claculate the number of words for each language in the text 
    """
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text) 
    counts = Counter(tokens)
    return counts

def detect_language(text):

    ratios = _calc_ratios(text)

    most_rated_language = max(ratios, key=ratios.get)
    most_common_words = ratios[most_rated_language]
    del ratios[most_rated_language]
    second_most_rated_language = max(ratios, key=ratios.get)
    second_most_common_words = ratios[second_most_rated_language]

    print ("The lengh of this text is %s" %(len(set(text))))
    print("the number of languages in this text is %s" %(_calc_ratios(text)))
    print("there is %s%% chances for this text to be writen in %s" %(_calc_probability(most_common_words, second_most_common_words), most_rated_language))
    



if __name__=='__main__':

    #text snipet from http://latta.blog.lemonde.fr/2017/02/08/goal-line-technology-un-nouveau-bug-contre-son-camp/
    text = '''Je m'appelle Angélica Summer, j'ai 12 ans et je suis canadienne. Il y a 5 ans, ma famille et moi avons déménagé dans le sud de la France. Mon père, Frank Summer, est mécanicien ; il adore les voitures anciennes et collectionne les voitures miniatures.'''
    detect_language(text)


# In[ ]:





# In[ ]:





# In[ ]:


#!/usr/bin/env python
#coding:utf-8
# Author: Hafid Mermouri
# Created: 09/02/2017

import sys

from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

def _calc_ratios(text):

    ratios = {}

    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    for lang in stopwords.fileids():
        stopwords_set = set(stopwords.words(lang))
        words_set = set(words)
        common_words = words_set.intersection(stopwords_set)

        ratios[lang] = len(common_words)

    return ratios


def detect_language(text):

    ratios = _calc_ratios(text)

    most_rated_language = max(ratios, key=ratios.get)
    most_common_words = ratios[most_rated_language]
    del ratios[most_rated_language]
    second_most_rated_language = max(ratios, key=ratios.get)
    second_most_common_words = ratios[second_most_rated_language]

    print("there is %s%% chances for this text to be writen in %s" %(_calc_probability(most_common_words, second_most_common_words), most_rated_language))


def _calc_probability(most, secode_most) :
    proba = (float(most) /(most + secode_most) * 100)
    return round(proba)

if __name__=='__main__':

    #text snipet from http://latta.blog.lemonde.fr/2017/02/08/goal-line-technology-un-nouveau-bug-contre-son-camp/
    text = '''
    Le match de Ligue 1 Bordeaux-Rennes, ce week-end, a été le théâtre du troisième incident significatif
    lié à l’usage de la Goal Line Technology depuis sa mise en œuvre dans divers championnats depuis deux saisons.
    La montre de l’arbitre central Sébastien Desiage a vibré à la 44e minute, indiquant que le ballon était
    entièrement entré dans la cage bordelaise au moment où le gardien Cédric Carrasso se saisissait de celui-ci,
    pourtant nettement devant la ligne de but. Sébastien Desiage a heureusement choisi d’ignorer l’alerte et de ne
    pas valider ce but virtuel, au grand soulagement du gardien des Girondins.
    '''

    detect_language(text)


# In[ ]:




