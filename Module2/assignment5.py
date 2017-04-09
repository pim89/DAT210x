import pandas as pd
import numpy as np
import os
curdir = os.path.dirname(__file__)

#
# TODO:
# Load up the dataset, setting correct header labels.
#
# .. your code here ..
filename = os.path.join(curdir,'Datasets','census.data')
print 'open file', filename
df = pd.read_csv(filename, names = ['education','age','capital-gain','race','capital-loss','hours-per-week','sex','classification'])
df['capital-gain'] = pd.to_numeric(df['capital-gain'], errors = 'coerce')
print df.head(5)
#
# TODO:
# Use basic pandas commands to look through the dataset... get a
# feel for it before proceeding! Do the data-types of each column
# reflect the values you see when you look through the data using
# a text editor / spread sheet program? If you see 'object' where
# you expect to see 'int32' / 'float64', that is a good indicator
# that there is probably a string or missing value in a column.
# use `your_data_frame['your_column'].unique()` to see the unique
# values of each column and identify the rogue values. If these
# should be represented as nans, you can convert them using
# na_values when loading the dataframe.
#
# .. your code here ..
print df.info()

#
# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal and nominal
# types using the methods discussed in the chapter.
#
# Be careful! Some features can be represented as either categorical
# or continuous (numerical). If you ever get confused, think to yourself
# what makes more sense generally---to represent such features with a
# continuous numeric type... or a series of categories?
#
# .. your code here ..
# ordinal features:
a = df.education.unique()
edorder = [a[11], a[10], a[8], a[6], a[4], a[9], a[2], a[12], a[1], a[5], a[0], a[3], a[7]]
a = df.classification.unique()
classorder = [a[0],a[1]]
df.education = df.education.astype("category", ordered=True, categories=edorder).cat.codes
df.classification = df.classification.astype("category", ordered=True, categories=classorder).cat.codes

# nominal features
df = pd.get_dummies(df,columns=['race'])
df = pd.get_dummies(df,columns=['sex'])
                                  
print df.head(10)
print df.info()
print df.columns


#
# TODO:
# Print out your dataframe
#
# .. your code here ..
print df

