#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

x = ["Ramesh", "Priya", "Suresh", "Akshay", "Roopa"]
y = [74,23,80,34,56]

plt.title("Students Marks Bar Graph")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.bar(x,y)

for(i,j) in zip(x,y):
    plt.annotate(j,(i,j))
plt.show()

