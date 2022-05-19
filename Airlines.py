import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:/Users/SHAJIUDDIN MOHAMMED/Desktop/EastWestAirlines.xlsx")
df.describe()

# Normalizing the data
def norm_func(i):
    x=(i-i.min()/i.std())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm =norm_func(df.iloc[:,1:])
df_norm.describe()

# for creating Dendogram 
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch 

z=linkage(df_norm,method="complete",metric="euclidean")

# Dendogram
plt.figure(figsize=(15,30));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel("Index");plt.ylabel("Distance")
sch.dendrogram(
    z,
    leaf_rotation=0.,
    leaf_font_size=10.,
)
plt.show()


# Now applying agglomerative clustering using clusters from dendogram
from sklearn.cluster import AgglomerativeClustering

h_complete=AgglomerativeClustering(n_clusters=5,affinity="euclidean",linkage="complete").fit(df_norm)
clusters_labels=pd.Series(h_complete.labels_)

df["clust"]=clusters_labels # creating a new column and assigning it to new column 

df_final=df.iloc[:,[0,12,1,2,3,4,5,6,7,8,9,10,11]]
df_final.head()

# Aggregate mean of each cluster
df.iloc[:, 2:].groupby(df.clust).mean()

# creating a csv file 
df_final.to_csv("AirlinesOutput_py.csv", encoding = "utf-8")

import os
os.getcwd()
