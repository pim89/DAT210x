# -*- coding: utf-8 -*-
"""
Created on Mon May 01 00:02:26 2017

@author: Pim
"""

from sklearn.decomposition import PCA
pca = PCA(n_components=2, svd_solver='full')
pca.fit(df)

PCA(copy=True, n_components=2, whiten=False)

T = pca.transform(df)
df.shape
T.shape