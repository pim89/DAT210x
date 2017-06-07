#
# This code is intentionally missing!
# Read the directions on the course lab page!
#
import pandas as pd
import numpy as np


x = pd.read_csv('Datasets/parkinsons.data')
x = x.drop('name',axis=1)
print x.head(5)
y = x.status
x = x.drop('status',axis=1)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x,y,random_state=7,test_size=0.3)

from sklearn.svm import SVC
model = SVC()
model.fit(X_train,y_train)
score = model.score(X_test,y_test)
print 'score = ',score

from sklearn.decomposition import PCA
from sklearn.manifold import Isomap
from sklearn.preprocessing import Normalizer,MaxAbsScaler,MinMaxScaler,KernelCenterer,StandardScaler
crange = np.arange(0.05,2,0.05)
grange = np.arange(0.001,0.1,0.001)
best_score = 0
for c in crange:
    for g in grange:
        for i in range(0,5):    
            if i==0:
                prep = Normalizer()
            if i==1:
                prep = MaxAbsScaler()
            if i==2:
                prep = MinMaxScaler()
            if i==3:
                prep = KernelCenterer()
            if i==4:
                prep = StandardScaler()                
            X_sc_train = prep.fit_transform(X_train)
            X_sc_test = prep.transform(X_test)    
            
            for j in range(2,6):
                for k in range(4,7):
                    #pca = PCA(n_components=j)
                    #X_sc_train2 = pca.fit_transform(X_sc_train)
                    #X_sc_test2 = pca.transform(X_sc_test)
                    isomap = Isomap(n_neighbors = j, n_components=k)
                    X_sc_train2 = isomap.fit_transform(X_sc_train)
                    X_sc_test2 = isomap.transform(X_sc_test)
                    model = SVC(C=c,gamma=g)
                    model.fit(X_sc_train2,y_train)
                    score = model.score(X_sc_test2,y_test)
                    if score>best_score:
                        print 'New C value = ', c
                        print 'New g value = ', g
                        print 'prep        = ', i
                        print 'New score   = ', score
                        best_score = score
    print '=====C=====',c