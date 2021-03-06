#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:32:27 2017

@author: ryad
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values

# Using the elbo meth to ginf the optimal number of cluster
from sklearn.cluster import KMeans
wcss = []
for i in range (1,11):
    kmeans = KMeans(n_clusters = i, init='k-means++' , max_iter = 300, n_init = 10 , random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)



#applying Kmean algo 
kmeans = KMeans(n_clusters = 5, init='k-means++' , max_iter = 300, n_init = 10 , random_state = 0)
y_kmeans =kmeans.fit_predict(X)

plt.scatter(X[y_kmeans == 0, 0] ,X[y_kmeans == 0, 1], s = 100 ,c= 'red' , label ='Cluseter 1')
plt.scatter(X[y_kmeans == 1, 0] ,X[y_kmeans == 1, 1], s = 100 ,c= 'blue' , label ='Cluseter 2')
plt.scatter(X[y_kmeans == 2, 0] ,X[y_kmeans == 2, 1], s = 100 ,c= 'black' , label ='Cluseter 3')
plt.scatter(X[y_kmeans == 3, 0] ,X[y_kmeans == 3, 1], s = 100 ,c= 'green' , label ='Cluseter 4')
plt.scatter(X[y_kmeans == 4, 0] ,X[y_kmeans == 4, 1], s = 100 ,c= 'yellow' , label ='Cluseter 5')
