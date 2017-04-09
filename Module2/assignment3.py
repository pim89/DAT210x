import pandas as pd
import os
curdir = os.path.dirname(__file__)
# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
filename = os.path.join(curdir,'Datasets','servo.data')
print 'open file', filename
df = pd.read_csv(filename, names=['motor','screw','pgain','vgain','class'])
print df.head(4)

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
slice1 = df[df.vgain == 5]
print 'number of vgain=5: ', len(slice1)

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
slice2 = df[(df.motor=='E') & (df.screw=='E')]
print 'number of motor and screw = E: ', len(slice2)

# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
slice3 = df[df.pgain==4]
meanvgain = slice3.vgain.mean()
print 'mean vgain of pgain=4: ', meanvgain

# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
print df.dtypes


