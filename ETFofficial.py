#!/usr/bin/env python
# coding: utf-8

# # Python project
# The purpose and goal with the analysis is to explore functions and syntax in python, 
# 
# to find information in the data and to be familiar with the fundamental basics infrastructures within python.
# 
# The report has conducted findings and insights.

# starting with the essentials

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import seaborn as sns


# Read data

# In[2]:


df = pd.read_csv('/Users/lucy/Documents/Vinter/merged_goldeikon.csv')


# # Describe Data set 
# when describing the dataset we get a summary and overview on it's context

# In[3]:


df.head(5)


# In[4]:


df.describe()


# # Exchange Traded Fund
# We can find information about the diffrent etf's and it's values

# In[5]:


df['ex_symbol'].head()


# In[6]:


df['ex_symbol'].unique()


# In[7]:


df['ex_symbol'].nunique()


# In[8]:


df["ex_symbol"].describe()


# In[ ]:


df["ex_symbol"].value_mean()


# In[9]:


df["ex_symbol"].value_counts()


# In[10]:


df.groupby(['ex_symbol','datetime']).mean().unstack(0)


# In[ ]:





# # matplotlib
# with these timeserie analyses we get an overview on the amount and close during the time interval. 

# In[11]:


df['datetime'] = pd.to_datetime(df['datetime'])


# In[12]:


df.plot.line(x='datetime', y='amount', colormap='viridis', grid=False)


# In[13]:


df.plot.line(x='datetime', y='close', colormap='viridis', grid=False)


# # 
# normal distribution

# In[29]:


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


# In[30]:


df.plot.hist(x='datetime', y='close', colormap='viridis', grid=False)


# In[31]:


x_min = 1.0
x_max = 1.7

mean = 1.0 
std = 4.3

x = np.linspace(x_min, x_max)

y = scipy.stats.norm.pdf(x,mean,std)


plt.plot(x,y, color='black')

