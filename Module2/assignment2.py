import pandas as pd
import os
curdir = os.path.dirname(__file__)
# TODO: Load up the 'tutorial.csv' dataset
#
# .. your code here ..
filename = os.path.join(curdir,'Datasets','tutorial.csv')
print 'open file', filename
df = pd.read_csv(filename)
print df
# TODO: Print the results of the .describe() method
#
# .. your code here ..
print 'describe method output:\n', df.describe()


# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
# .. your code here ..
slice1 = df.loc[2:4,['col3']]
print slice1