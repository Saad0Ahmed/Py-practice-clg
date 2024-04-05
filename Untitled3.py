#!/usr/bin/env python
# coding: utf-8

# In[2]:


import statistics

sample = [130, 137, 136, 142, 135]

var = statistics.pvariance(sample)
print("The Variance is ", var)

sd = statistics.pstdev(sample)
print("The Standard Deviation is ", sd)

