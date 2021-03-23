#!/usr/bin/env python
# coding: utf-8

# # Python project 
# 
# The purpose and goals with this report is to explore with functions and syntax in python, 
# 
# to find information in the data and to learn the fundamental basics infrastructures within python.
# 
# The analysis has conducted findings and insicts.
# 

# starting with the dependencies

# In[44]:


import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


# In[45]:


df = pd.read_csv('/Users/lucy/Documents/Vinter/merged_goldeikon.csv')


# # Describe Data set 
# when describing the dataset we get a summary and overview on the dataset and it's context

# In[46]:


df.head(5)


# In[47]:


df.describe()


# In[48]:


df.index


# In[49]:


df.set_index('ex_symbol')


# # Exchange Traded Fund
# We can find information about the diffrent etf's and it's values

# In[50]:


df['ex_symbol'].head()


# In[52]:


df.dtypes


# In[53]:


df['ex_symbol'].unique()


# In[54]:


df['ex_symbol'].nunique()


# In[55]:


df["ex_symbol"].describe()


# In[56]:


df["ex_symbol"].value_counts()


# In[57]:


exsymbol_df = pd.DataFrame( {     
"exsymbol" : ['l_gbsx', 'l_xgld', 'l_igln', 'l_sgld', 'l_phau', 'l_sgbs', 's_csgold', 's_zgldus', 's_sgld', 's_xgld'] ,
"value" : [1289, 1289, 1289, 1289, 1289, 1280, 1279, 1279, 1005, 680]
})
exsymbol_df.head()


# In[58]:


df.groupby(['ex_symbol','datetime']).mean().unstack(0)


# # matplotlib
# Here we get an view on the amount and close during the time interval

# In[64]:


df['datetime'] = pd.to_datetime(df['datetime'])


# In[65]:


df.plot.line(x='datetime', y='amount', colormap='viridis', grid=False)


# In[66]:


df.plot.line(x='datetime', y='close', colormap='viridis', grid=False)


# # 
# mean and standard diviation for amount in the normal distribution

# In[67]:


x_min = 1.0
x_max = 1.7

mean = 1.0
std = 4.3

x = np.arange(-14, 14, 0.0014)

y = scipy.stats.norm.pdf(x,mean,std)

plt.ylim(0,0.15)

plt.title('normal distribution of amount with matplotlib',fontsize=10)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("normal.png")
plt.plot(x,y, color='black')

