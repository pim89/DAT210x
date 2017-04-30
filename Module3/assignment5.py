import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import parallel_coordinates, andrews_curves
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
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# Also get rid of the 'area' and 'perimeter' features
# 
# .. your code here ..
df = df.drop('area',1)
df =df.drop('perimeter',1)


#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
# .. your code here ..
parallel_coordinates(df,'wheat_type', alpha = 0.5)
andrews_curves(df,'wheat_type', alpha = 0.5)


plt.show()


