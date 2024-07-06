import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering
import spacy
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

def preprocess(text):
        text = text.lower()  # Convert to lowercase
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        text = re.sub(r'\d+', '', text)  # Remove digits
        text = re.sub(r'\s+', ' ', text)  # Remove extra whitespaces
        return text

def Des_Clustering(data1,Num=None,distance_threshold1=None,dict1=[]):
    Desc=[]
    Info=[]
    for i, aa in enumerate(data1):
        Desc1=aa['description']+' '+aa['Full_name']+' '+aa['User-name']
        Desc.append(Desc1)
        Info1={'Username':aa['User-name'],'description':Desc1}
        Info.append(Info1)
#------------------------------------------------------------------------------------------------------------------#
    sentences=Desc
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(sentences)
    agg_clustering = AgglomerativeClustering(n_clusters=Num, affinity='euclidean', linkage='ward',distance_threshold=distance_threshold1)
    agg_clustering.fit(X.toarray())
    final_list=[]
#------------------------------------------------------------------------------------------------------------------#
    for i in range(len(sentences)):
        lis=[]
        #print("Cluster ", i, ":")
        for j in range(len(sentences)):
            if agg_clustering.labels_[j] == i:
                for s,ss in enumerate(Info):
                    if ss['description']==sentences[j]:
                        lis.append(ss['Username'])
#------------------------------------------------------------------------------------------------------------------#                    
        dict={f"Cluster# ":i,'List':lis}
        if dict['List']!=[]: 
            final_list.append(dict)
    #print(final_list)    
    return final_list 
def Name_Extract(string):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(string)
    names = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
#------------------------------------------------------------------------------------------------------------------#
def DB_Clustering():
    with open('data.txt', 'r',encoding='utf-8') as f:
        data = f.readlines()
# Preprocess data
    data = [preprocess(sentence) for sentence in data]
    # Feature extraction and dimensionality reduction
    #print(data)
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(data)

    svd = TruncatedSVD(n_components=2, random_state=42)
    X_reduced = svd.fit_transform(X)

    # Clustering
    #kmeans = KMeans(n_clusters=3, random_state=42)
    agglomerative = AgglomerativeClustering(distance_threshold=4)
    #dbscan = DBSCAN(eps=0.5, min_samples=2)

    models = [('Agglomerative', agglomerative)]

    # Fit models and predict cluster labels
    fig, axs = plt.subplots(1, len(models), figsize=(15, 5))

    for i, (name, model) in enumerate(models):
        if name == 'DBSCAN':
            labels = model.fit_predict(X_reduced)
        else:
            labels = model.fit_predict(X.toarray())
        axs[i].scatter(X_reduced[:, 0], X_reduced[:, 1], c=labels, cmap='viridis')
        axs[i].set_title(name)
    plt.show()

    # Print clusters
    for i, (name, model) in enumerate(models):
        if name == 'DBSCAN':
            labels = model.fit_predict(X_reduced)
        else:
            labels = model.fit_predict(X.toarray())
        print(f'Clusters for {name}:')
        for j in range(max(labels) + 1):
            cluster_text = [data[k] for k in range(len(data)) if labels[k] == j]
            print(f'Cluster {j}:')
            print(cluster_text)
            print()
#DB_Clustering()
#    print(agg_clustering)
#Des_Clustering(sentences,None,2)