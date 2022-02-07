#!/usr/bin/env python
# coding: utf-8

# Programming Assignment 8
# *************************************

# 1.Write a Python Program to Add Two Matrices?

# In[67]:


Matrix_A = [[1,2,3],
            [4,5,6],
            [7,8,9]]

Matrix_B = [[1,2,3],
            [4,5,6],
            [7,8,9]]
c = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(3):
    for j in range(3):
        c[i][j] = Matrix_A[i][j] + Matrix_B[i][j]
         
        
for k in c:
    print(k)


    


# ****

# 2.Write a Python Program to Multiply Two Matrices?

# In[68]:


Matrix_A = [[1,2,3],
            [4,5,6],
            [7,8,9]]

Matrix_B = [[1,2,3],
            [4,5,6],
            [7,8,9]]
c = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(3):
    for j in range(3):
        c[i][j] = Matrix_A[i][j] * Matrix_B[i][j]
         
        
for k in c:
    print(k)


# ****

# 3.Write a Python Program to Transpose a Matrix?

# In[76]:


A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

for i in range(3):
    for j in range(3):
        c[j][i] = A[i][j]

print('Transpose: ')
for k in c:
    print(k)


# ****

# 4.Write a Python Program to Sort Words in Alphabetic Order?

# In[113]:


lis = input().split(",")
print(sorted(lis))


# ****

# 5.Write a Python Program to Remove Punctuation From a String?

# In[151]:


import string
s = list(input())
p = string.punctuation
for i in p:
    for j in s:
        if i == j: s.remove(j) 

print('\nPunctuation list: ',p,end=" ")
print('\n')
# for k in s:
#     print(k,end=" ")
print("".join(s))

