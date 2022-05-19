import pandas as pd
import matplotlib.pylab as plt

Crime = pd.read_csv("C:/Users/SHAJIUDDIN MOHAMMED/Desktop/crime_data.csv")
Crime.columns = 'State','Murder', 'Assault', 'UrbanPop','Rape'

Crime.describe()

# Normalization function 
def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(Crime.iloc[:, 1:])
df_norm.describe()

# for creating dendrogram 
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch 

z = linkage(df_norm, method = "complete", metric = "euclidean")

# Dendrogram
plt.figure(figsize=(15, 8));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(z, 
    leaf_rotation = 0,  # rotates the x axis labels
    leaf_font_size = 10 # font size for the x axis labels
)
plt.show()


# Now applying AgglomerativeClustering choosing 5 as clusters from the above dendrogram
from sklearn.cluster import AgglomerativeClustering

h_complete = AgglomerativeClustering(n_clusters = 5, linkage = 'complete', affinity = "euclidean").fit(df_norm) 
h_complete.labels_

cluster_labels = pd.Series(h_complete.labels_)

Crime['clust'] = cluster_labels # creating a new column and assigning it to new column 

Crime_final = Crime.iloc[:, [5,0,1,2,3,4]]
Crime_final.head()

# Aggregate mean of each cluster
Crime_final.iloc[:, 2:].groupby(Crime_final.clust).mean()

# creating a csv file 
Crime_final.to_csv("Crimepython_output.csv", encoding = "utf-8")

import os
os.getcwd()
