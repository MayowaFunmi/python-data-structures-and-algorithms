#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Example of Series
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index=[1, 2, 3, 4])
s


# In[3]:


# Example of DataFrame
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
df


# In[7]:


data2 = [['Alex', 10], ['Bob', 12], ['Clarke', 33]]
df1 = pd.DataFrame(data2, columns=['Name', 'Age'], index=[1, 2, 3])
df1


# In[9]:


data3 = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 54, 87, 12], 'Occupation':['Teacher', 'Accountant', 'Engineer', 'Doctor']}
df2 = pd.DataFrame(data3, index=[1, 2, 3, 4])
df2


# In[11]:


data4 = [{'a': 1, 'b': 2, 'd': 4}, {'a': 5, 'b': 10, 'c': 20, 'd': 55}]
df3 = pd.DataFrame(data4, index=[1, 2])
df3


# In[13]:


# examples of panel
data5 = [10, 20, 30]
data5


# In[ ]:


# panel class has been removed


# In[15]:


# reading data from csv file
df5 = pd.read_csv('/home/mayowafunmi/Documents/udemy-data-science/Section 1/hrdata.csv')
df5


# In[18]:


df5['Name']


# In[19]:


df5['Salary'] # double brackets shows heading/name of colum


# In[20]:


salary = df5['Salary']
sum(salary)


# In[23]:


df5[['Salary', 'Name']]


# In[28]:


# generate one random row
df5.sample(n=1)


# In[ ]:





# In[29]:


df5.shape


# # Adding new column in dataframe

# In[30]:


number_of_leaves = [0, 2, 0, 7, 3, 2]
df5['Leaves Taken'] = number_of_leaves
df5


# In[31]:


df5.shape


# In[32]:


gender = ['M', 'F', 'M', 'M', 'F', 'M']
df5['Gender'] = gender
df5


# In[33]:


del df5['Gender']
df5


# In[5]:


import pandas as pd
file = pd.read_csv('/home/mayowafunmi/Documents/udemy-data-science/Section 1/Cricket.csv')
file


# In[4]:


# display only first five elements of the data
file.head()


# In[6]:


# display only last five elements
file.tail()


# In[7]:


file['Delivery'].head()


# In[9]:


# display first 10 elements
file.head(10)


# In[12]:


# get specific element in the table
file['score_india'][5]


# # Sorting the DataFrame based on a column

# In[14]:


# rearrange values given the parameters for rearrangement
file.sort_values('score_india')


# In[15]:


file.sort_values('score_pk')


# In[17]:


# sort in descending order, ascending order is default
file.sort_values('score_pk', ascending=False)


# In[18]:


# count number of unique values that occur in dataset or in a column
file.nunique()


# In[19]:


sum(file['score_india'])


# # Indexing Using Labels in pandas

# In[20]:


# using loc()
file


# In[25]:


# select row number 4 data
file.loc[4]


# In[27]:


# select from row 1 to 4
file.loc[1:4]


# In[29]:


# select first five rows including 5th index and every columns of the file
file.loc[0:5, :]


# In[31]:


# select from 5th row onwards
file.loc[5:, :]


# In[32]:


# computes various summary statistics
file.describe()


# # Filtering under one condition

# In[35]:


# select all rows with a condition
# show boolean values of >= 2 condition 
filter1 = file['score_india'] >= 2


# In[36]:


filter1


# In[37]:


# show the table with elements >= 2
file[filter1]


# # Selecting rows with indices using "iloc"

# In[46]:


# select rows with indices 0 and 5 only
file.iloc[[2, 5]] # same as using loc[[2, 5]]


# In[53]:


# select rows with particular indices and particular colums
# ist array select rows, second array select colums
file.iloc[[0, 2, 4, 6, 8, 10], [1, 2]]


# In[ ]:




