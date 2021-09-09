import numpy as np
n, p = [int(x) for x in input().split()] #it taking first two input of n and p
x= [] # array for the list

for i in range(n): # taking input for each row
    x.append(input().split()) # taking input and spliting the data into columnwise input

arr = np.array(x) # making this numpy array
arr = arr.astype(np.float16)#making data type into float

mn = arr.mean(axis = 1) # having mean value in rowwise  with axis = 1
mean= mn.round(2) #as output need to be two value after point value
print(mean)