#!/usr/bin/env python
# coding: utf-8

# # Python project 
# 
# The purpose and goals with this analysis is to explore with functions and syntax in python, 
# 
# to find information in the data and to learn the fundamental basics infrastructures within python.
# 
# The report has conducted findings and insicts.
# 
# 
# 

# starting with the dependencies

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


# Read data

# In[3]:


df = pd.read_csv('/Users/lucy/Documents/Vinter/merged_goldeikon.csv')


# # Describe Data set 
# when describing the dataset we get a summary and overview on the dataset and it's context

# In[4]:


df.head(5)


# In[5]:


df.describe()


# # Exchange Traded Fund
# We can find information about the diffrent etf's and it's values

# In[6]:


df['ex_symbol'].head()


# In[7]:


df['ex_symbol'].unique()


# In[8]:


df['ex_symbol'].nunique()


# In[9]:


df["ex_symbol"].describe()


# In[10]:


df["ex_symbol"].value_counts()


# In[11]:


df.groupby(['ex_symbol','datetime']).mean().unstack(0)


# # matplotlib
# Here we get an view on the amount and close during the time interval

# In[64]:


df['datetime'] = pd.to_datetime(df['datetime'])


# In[69]:


df.plot.line(x='datetime', y='amount', colormap='viridis', grid=False)


# In[70]:


df.plot.line(x='datetime', y='close', colormap='viridis', grid=False)


# # 
# mean and standard diviation for amount in the normal distribution

# In[71]:


x_min = 1.0
x_max = 1.7

mean = 1.0
std = 4.3

x = np.arange(-14, 14, 0.0014)

y = scipy.stats.norm.pdf(x,mean,std)

plt.ylim(0,0.15)

plt.title('normal distribution with matplotlib',fontsize=10)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("normal.png")
plt.plot(x,y, color='black')

