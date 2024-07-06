import nltk
from nltk import word_tokenize, pos_tag
from namematcher import NameMatcher
# -*- coding: utf-8 -*-

from namematcher import NameMatcher
name_matcher = NameMatcher()
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json
import difflib
def Names(name1, name2):
    """
    Check if two names are alike using difflib library.
    
    Args:
        name1 (str): First name to compare.
        name2 (str): Second name to compare.
            
    Returns:
        bool: True if names are alike, False otherwise.
    """
    similarity_score = difflib.SequenceMatcher(None, name1.lower(), name2.lower()).ratio()
    #similarity_score >= 0.8
    if similarity_score >= 0.8:
        return True
    else:
        return False

#name1 = "Omar Sarfaraz Cheema"
#name2 = "Omer Sarfaraz Chema"

def extract_description(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    nouns = [word for word, pos in tagged if pos in ['NN', 'NNP', 'NNS', 'NNPS']]
    nouns =",".join(nouns)
    nouns = '"'+nouns+'"'
    return nouns

def similarity(list1, list2):
    list1=extract_description(list1)
    #print(list1)
    list2=extract_description(list2)
    #print(list2)
    try:
        common = len(set(list1) & set(list2))
        total = len(set(list1) | set(list2))
    except Exception as e:
        print('')
    return (common/total)*100

def Description_Analysis(sentence_1,sentence_2):


            
#   print(people1)
#for i, user in enumerate(fakepeople):
    #print(user["Full_name"], "Description is: ", user["description"])
    #sentence_1 = #people1["description"]
    #sentence_2 = #user["description"]
   # sentence_1 = "This is parody account Imran Khan"
    #sentence_2 = "This is support account account of Imran Khan."
    try:
        keywords = extract_description(sentence_1)#.encode('utf-8')

        pop_names = extract_description(sentence_2)#.encode('utf-8')


        #sample_names = keywords

        #count = 0
        #average = 0
        #matches = name_matcher.find_closest_names(sample_names, pop_names)
    except Exception as e:
        print('--error in func1--',e)
    try:
        #for i in range(len(matches)):
        #    orig_name = sample_names[i]
        #    pop_name, pop_index, score = matches[i]
        #    if score >0.5:
        #        count = count + 1
        #        #print('For name: %s, best match: %s, score %f' % (orig_name, pop_name, score))
        #        average = average + score

        #average = average/count
        vectorizer = CountVectorizer().fit_transform([sentence_1, sentence_2])
        similarity = cosine_similarity(vectorizer)[0][1]
    except Exception as e:
        print('--error in func--',e)
    return similarity#,average
    
#name_matcher = NameMatcher()

#helo=name_matcher.match_names('Naeem ul Haque','Imran Khan')
#print(helo*100)
#sentence = "The dog is playing in the park."
#nouns = extract_description(sentence)
#print(nouns)
import re

