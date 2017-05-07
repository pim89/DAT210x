import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import os
# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
samples = [];
colors = [];
#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 
imdir = 'Datasets/ALOI/32'
for i in os.listdir(imdir):
    im = misc.imread(os.path.join(imdir,i))
    samples.append(im.reshape(-1))
    colors.append('b')
    
#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 
imdir = 'Datasets/ALOI/32i'
for i in os.listdir(imdir):
    im = misc.imread(os.path.join(imdir,i))
    samples.append(im.reshape(-1))
    colors.append('r')
#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 
df = pd.DataFrame(samples)

#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 
from sklearn.manifold import Isomap
isomap = Isomap(n_neighbors=6, n_components=3)
isomap.fit(df)
T = isomap.transform(df)

#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Isomap: 0-1')
ax.set_xlabel('Component: {0}'.format(0))
ax.set_ylabel('Component: {0}'.format(1))
ax.scatter(T[:,0],T[:,1], marker='.',alpha=0.7, c=colors)

#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_title('Isomap: 0-1')
ax.set_xlabel('Component: {0}'.format(0))
ax.set_ylabel('Component: {0}'.format(1))
ax.set_zlabel('Component: {0}'.format(2))
ax.scatter(T[:,0],T[:,1],T[:,2], marker='.',alpha=0.7, c= colors)


plt.show()

