from pprint import pprint
import nltk
from namematcher import NameMatcher
from nltk import word_tokenize, pos_tag
import json
from Des import extract_description, Description_Analysis,similarity
import mysql.connector
from Clustering import Des_Clustering
import spacy
import pandas as pd
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from Description1 import group_Description

def Feedback():
    cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaguar@123",
    database="sql_false_flag")
    cursor = cnx.cursor()
    query = "SELECT * FROM Feed_Back_Groups1_Info"
    cursor.execute(query)
    Feedback_Info=cursor.fetchall()
    Final_Dict=[]
#------------------------------------------------------------------------------------------------------------------#
    for feed in Feedback_Info:
        if feed[2]=='':
            fedd='Not_Found'
        else:
            fedd=feed[2]
        dict1={'Fullname':feed[0],'description':feed[1],'Twitter_ID':'@'+fedd.lower(),'User_Pics':feed[3]}
        Final_Dict.append(dict1)
#------------------------------------------------------------------------------------------------------------------#
    group_Description(Final_Dict)    
    #query = "SELECT * FROM Feed_Back_Groups1_Info"
    #Feedback_Information = pd.read_sql(query, cnx)    
    #print(Feedback_Information['Username'] )
    #query = "SELECT * FROM Feed_Back_Groups1_Info"
    #Information = pd.read_sql(query, cnx)
    #Information=list(Information['Description'])
    #print(Information)

    
# Example sentences
    #sentences = [
    #    "I love reading books",
    #    "Reading books is my hobby",
    #    "I love reading novels",
    #    "Novels are my favorite",
    #    "I love reading science fiction",
    #    "Science fiction is my favorite genre",
    #    "I hate sports",
    #    "I don't like sports"
    #]

    # Create a Pandas DataFrame to store the sentences
    
    ## Vectorize the sentences using TF-IDF
    #vectorizer = TfidfVectorizer()
    #tfidf_matrix = vectorizer.fit_transform(df['sentences'])

    ## Perform dimensionality reduction using PCA
    #pca = PCA(n_components=2)
    #pca_matrix = pca.fit_transform(tfidf_matrix.toarray())

    ## Compute cosine similarity between each sentence and the first sentence
    #similarity_scores = cosine_similarity(tfidf_matrix[0], tfidf_matrix)

    ## Perform clustering using K-means
    #kmeans = KMeans(n_clusters=16)
    #kmeans.fit(pca_matrix, similarity_scores[0])

    ## Print the clusters and the sentences in each cluster
    #for i in range(kmeans.n_clusters):
    #    cluster = pca_matrix[kmeans.labels_ == i]
    #    sentences = df['sentences'][kmeans.labels_ == i]
    #    print(f'Cluster {i}: {sentences.to_list()}')
    #    print('|||||||')




#Feedback()