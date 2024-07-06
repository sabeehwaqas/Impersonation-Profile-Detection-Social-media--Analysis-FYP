# -*- coding: utf-8 -*-

from namematcher import NameMatcher
name_matcher = NameMatcher()
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json

def extract_keywords(sentence):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)
    pronouns = ["i", "me", "my", "mine", "myself", "you", "your", "yours", "yourself", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "we", "us", "our", "ours", "ourselves", "they", "them", "their", "theirs", "themselves"]
    keywords = [word for word in words if word.lower() not in pronouns]
    keywords = [word for word in words if word.lower() not in stop_words]
    return keywords

def Description_Analysis(sentence_1,sentence_2):


            
#   print(people1)
#for i, user in enumerate(fakepeople):
    #print(user["Full_name"], "Description is: ", user["description"])
    #sentence_1 = #people1["description"]
    #sentence_2 = #user["description"]
    sentence_1 = "This is parody account Imran Khan"
    sentence_2 = "This is support account account of Imran Khan."

    keywords = extract_keywords(sentence_1)#.encode('utf-8')

    pop_names = extract_keywords(sentence_2)#.encode('utf-8')


    sample_names = keywords

    count = 0
    average = 0
    matches = name_matcher.find_closest_names(sample_names, pop_names)
    for i in range(len(matches)):
        orig_name = sample_names[i]
        pop_name, pop_index, score = matches[i]
        if score >0.5:
            count = count + 1
            #print('For name: %s, best match: %s, score %f' % (orig_name, pop_name, score))
            average = average + score

    average = average/count
    vectorizer = CountVectorizer().fit_transform([sentence_1, sentence_2])
    similarity = cosine_similarity(vectorizer)[0][1]

    #if similarity > 0.4:
    #    print("Sentences are semantically equivalent.")
    #else:
    #    print("Sentences are semantically different.")

    print("The average percentage of similarity in keywords: ", average,"\nSemantically similar: ",similarity)
#Description_Analysis('Hello world','Hello world')