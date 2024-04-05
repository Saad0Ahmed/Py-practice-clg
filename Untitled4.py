#!/usr/bin/env python
# coding: utf-8

# In[1]:


file = open("4.txt", "r")
lines = file.readlines()

for x in lines:
    print(x)
file.close()

