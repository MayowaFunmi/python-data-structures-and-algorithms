#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import time
import sys


# # compare python list size and numpy size

# In[8]:


b = range(1000)
print(sys.getsizeof(5) * len(b))


# In[7]:


c = np.arange(1000)
print(c.size * c.itemsize)


# # # compare python list speed and numpy speed

# In[9]:


size = 100000


# # for python list

# In[13]:


l1 = range(size)
l2 = range(size)
start = time.time()
result = [(x + y) for x, y in zip(l1, l2)]
result = [(x + y) for x, y in zip(l1, l2)]
#print(result)
print("Python list took:", (time.time() - start) * 1000)


# # for numpy

# In[20]:


a1 = np.arange(size)
a2 = np.arange(size)
start = time.time()
result = a1 + a2
print("Numpy array took:", (time.time() - start) * 1000)


# # numpy tutorial

# In[22]:


a = np.array([1, 2, 3, 4, 5])
b = np.array([-4, 6, 0])
print('a= ', a)
print('b= ', b)


# In[23]:


type(a)


# In[24]:


a.dtype


# In[25]:


b.dtype


# In[31]:


# declare the datatype of variables
#a = np.array([1, 2, 3, 4, 5], dtype='i')
#b = np.array([-4, 6, 0], dtype='f')


# In[48]:


c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
e = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [-3, 4, 9]])

c.ndim


# In[35]:


d.ndim


# In[44]:


e


# In[41]:


e[3,0]


# In[42]:


f = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
f


# In[43]:


f.ndim


# In[45]:


f[1, 0]


# In[46]:


f[1, 0, 2]


# In[49]:


c.shape


# In[50]:


d.shape


# In[51]:


e.shape


# In[53]:


f.shape 
# 2 horizontal rows i.e each a 2 dim array and a 3 by 3 shape


# In[54]:


f.shape[0] # total number of 2 dim arrays


# In[55]:


f.shape[1]
# in each 2d array, how many 1 d arrays?


# In[56]:


f.shape[2]
# in each 1 d array, how many elements?


# In[57]:


f.shape[0], f.shape[1], f.shape[2]


# In[58]:


e.size


# In[59]:


f.size # how many elements in the array


# In[62]:


e.nbytes # how many bytes is taken in the memory


# In[63]:


f.nbytes


# In[64]:


a.nbytes


# In[66]:


f.mean


# # arange, random.permutation, reshape

# In[67]:


A = np.arange(100)
A


# In[68]:


B = np.arange(20, 75)
B


# In[71]:


C = np.arange(20, 51, 5)
C


# In[73]:


A = np.random.permutation(np.arange(10))
A


# In[77]:


get_ipython().run_line_magic('pinfo', 'np.random.randint')


# In[81]:


np.random.randint(20, 300) # generates a single number


# In[90]:


x = np.random.rand(1000) # generates 1dim array of 1000 numbers between 0 and 1
x


# In[91]:


import matplotlib.pyplot as plt
plt.hist(x)


# In[92]:


plt.hist(x, bins=10)


# In[93]:


y = np.random.randn(100000)
y


# In[94]:


plt.hist(y, bins=200)


# In[96]:


v = np.random.rand(2, 3) # shape(2, 3) array of numbers btw 0 and 1
v


# In[97]:


v.ndim


# In[100]:


m = np.random.rand(2, 3, 4)
m


# In[101]:


m.ndim


# In[103]:


m = np.random.rand(2, 3, 4, 2)
m


# In[104]:


m.ndim


# # Reshape

# In[105]:


x = np.arange(20)
x


# In[108]:


x.reshape(2,10)


# In[109]:


x.reshape(4, 5)


# In[110]:


x.reshape(2, 2, 5)


# # numpy slicing

# In[114]:


x = np.arange(100)
b = x[3:10]
b


# In[115]:


b[2] = 200
b


# In[117]:


# this also changes the element in x because the same memory is accessed in numpy
# To ensure x is not affected and create another memory for b
b = x[3:10].copy()
b


# In[122]:


x = np.arange(100)
x[::2] # from start to end and step 5


# In[124]:


x[::-5] # from start to x and reverse step 5


# In[128]:


x[4] = 1200
x


# In[131]:


idx = np.argwhere(x==1200)[0][0] # get the index of an element in an array
idx


# In[135]:


t = np.round(10*np.random.rand(5, 4))
t


# In[136]:


t.ndim


# In[137]:


t.shape


# In[139]:


t[2,1] # 3rd array and 2nd element i.e 3rd row 2nd column


# In[142]:


t[:, 1] # all rows 2nd column


# In[145]:


t[3] # 3rd row array 


# In[146]:


t[3:] # from 3rd array inclusive to the end


# In[147]:


t[:2] # from beginning to 2nd array excluding the 2nd array


# In[149]:


t[1:4] # from 1st array inclusive to 4th array excluding


# In[152]:


t[1:3, 2:4] #rows in 1st and 2nd arrays, then 2nd and 3th rows in that arrays


# In[153]:


t


# In[154]:


t.T # t transpose


# In[155]:


t.transpose


# In[158]:


import numpy.linalg as la
d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
la.inv(d)


# In[159]:


la.inv(np.random.rand(3,3))


# In[160]:


get_ipython().run_line_magic('whos', '')


# In[161]:


t


# In[162]:


t.sort(axis=0) # sort individual column element in acsending order


# In[163]:


t


# In[164]:


t.sort(axis=1) # sort individual row element in acsending order
t


# In[ ]:




