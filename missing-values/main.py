import numpy as np
# import panndas
import pandas as pd 

lst = [float(x) if x != 'nan' else np.NaN for x in input().split()]

# turn lst into an np array
arr = np.asarray(lst)
# turn the np array into a pd series
pd = pd.Series(arr)
# use buitl in pd function to fill in missing values with series mean
p=pd.fillna(pd.mean().round(1))

print(p)