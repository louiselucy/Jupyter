#!/usr/bin/env python
# coding: utf-8

# In[63]:


import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


# In[64]:


df = pd.read_csv('/Users/lucy/Documents/Vinter/merged_goldeikon.csv')


# # Describe Data set
# here we get a quick wiev on the dataset and it's context

# In[65]:


df.head(5)


# In[66]:


df.describe()


# # Exchange Traded Fund
# here we can find information about the diffrent etf's and it's values

# In[67]:


df['ex_symbol'].unique()


# In[68]:


df['ex_symbol'].nunique()


# In[69]:


df["ex_symbol"].describe()


# In[70]:


s = pd.Series(['l_sgld', 's_sgld', 'l_igln', 'l_xgld', 's_xgld', 'l_gbsx', 'l_phau', 's_csgold', 'l_sgbs', 's_zgldus'])
s.describe()


# In[71]:


df["ex_symbol"].value_counts()


# In[72]:


exsymbol_df = pd.DataFrame( {     
"exsymbol" : ['l_gbsx', 'l_xgld', 'l_igln', 'l_sgld', 'l_phau', 'l_sgbs', 's_csgold', 's_zgldus', 's_sgld', 's_xgld'] ,
"value" : [1289, 1289, 1289, 1289, 1289, 1280, 1279, 1279, 1005, 680]
})
exsymbol_df.head()


# # matplotlib
# here we get a overview of the amount and close in the same graph during the time interval
# https://matplotlib.org/3.2.2/gallery/misc/plotfile_demo_sgskip.html , https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0 , https://moonbooks.org/Articles/How-to-plot-a-normal-distribution-with-matplotlib-in-python-/ 

# In[73]:


df.plot.line(x='datetime', y=['close', 'amount'])


# In[74]:


df.describe()


# In[77]:


x_min = 1.0
x_max = 1.7

mean = 1.0
std = 4.3

x = np.linspace(x_min, x_max, 100)

y = scipy.stats.norm.pdf(x,mean,std)

plt.title('Half normal distribution of amount with matplotlib',fontsize=10)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("half_normal.png")

plt.plot(x,y, color='black')

