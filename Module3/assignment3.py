import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import os
curdir = os.path.dirname(__file__)
filename = os.path.join(curdir,'Datasets','wheat.data')

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')
#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
df = pd.read_csv(filename,index_col=0)

#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
# .. your code here ..
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('area')
ax.set_ylabel('perimeter')
ax.set_zlabel('asymmetry')
ax.scatter(df['area'],df['perimeter'],df['asymmetry'], c='r', marker = 'o')
#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
# .. your code here ..
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection = '3d')
ax2.set_xlabel('width')
ax2.set_ylabel('groove')
ax2.set_zlabel('length')
ax2.scatter(df['width'],df['groove'],df['length'], c = 'g')


plt.show()


