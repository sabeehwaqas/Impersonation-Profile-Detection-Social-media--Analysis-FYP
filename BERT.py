from sklearn.cluster import DBSCAN
import numpy as np
import Levenshtein
import mysql.connector
# Example list of names
names = ['Imran Khan Official', 'Imran Khan', 'Imran Khan Niazi', 'Imran Ahmed Khan', 'Syed Imran Khan', 'ALAN WALKER']

import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from Levenshtein import distance
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaguar@123",
    database="sql_false_flag")
cursor = cnx.cursor()
query = "SELECT Fullname FROM UsersProfile"
cursor.execute(query)
rows = cursor.fetchall()
#print(rows)
rows1=[]
for row in rows:
    text = row[0][:-1]
    rows1.append(text)
# Load the data
#names = pd.read_csv("names.csv")["name"].tolist()

# Calculate the distance matrix using Levenshtein distance
#dist_matrix = np.zeros((len(rows1), len(rows1)))
#for i in range(len(rows1)):
#    for j in range(len(rows1)):
#        dist_matrix[i, j] = distance(rows1[i], rows1[j])

## Cluster the names using hierarchical clustering
#clustering = AgglomerativeClustering(n_clusters=20, affinity="precomputed", linkage="average", distance_threshold=None)
#clusters = clustering.fit_predict(dist_matrix)

## Print the clusters
#for i in range(max(clusters)+1):
#    print(f"Cluster {i}: {np.array(names)[np.where(clusters == i)[0]].tolist()}")
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

data=rows1
data11=[]
# Preprocess the data
#data["name"] = data["name"].str.lower().str.replace('[^\w\s]','')
#data["name_tokens"] = data["name"].str.split()
for data1 in data:
    data11.append(data1.split())
# Extract features
#data['name_tokens']=data11
for i in data11:
    vectorizer = TfidfVectorizer(analyzer="word", ngram_range=(1,2), min_df=2, max_df=0.5)
    features = vectorizer.fit_transform(i)

# Reduce dimensionality
from sklearn.decomposition import TruncatedSVD
svd = TruncatedSVD(n_components=100, random_state=42)
features = svd.fit_transform(features)

# Cluster the data
kmeans = KMeans(n_clusters=10, random_state=42)
clusters = kmeans.fit_predict(features)

# Print the clusters
for i in range(10):
    print(f"Cluster {i}: {data.iloc[np.where(clusters == i)[0], 0].tolist()}")
