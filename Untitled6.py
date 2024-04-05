#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt

x = ["Ramesh", "Priya", "Suresh", "Akshay", "Roopa"]
y = [74,23,80,34,56]

plt.title("Students Marks Pie Graph")

plt.pie(y,labels=x,autopct='%d')

plt.show()

