#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import matplotlib.pyplot as plt


# In[9]:


df = pd.read_csv('/Users/lucy/Documents/Vinter/merged_goldeikon.csv')


# # Describe Data set 
# here we get a quick wiev on the dataset and it's context

# In[10]:


df.head(5)


# In[11]:


df.describe()


# # Exchange Traded Fund
# here we can find information about the diffrent etf's and it's values

# In[12]:


df['ex_symbol'].unique()


# In[13]:


df['ex_symbol'].nunique()


# In[14]:


df["ex_symbol"].describe()


# In[15]:


s = pd.Series(['l_sgld', 's_sgld', 'l_igln', 'l_xgld', 's_xgld', 'l_gbsx', 'l_phau', 's_csgold', 'l_sgbs', 's_zgldus'])
s.describe()


# In[16]:


df["ex_symbol"].value_counts()


# In[17]:


exsymbol_df = pd.DataFrame( {     
"exsymbol" : ['l_gbsx', 'l_xgld', 'l_igln', 'l_sgld', 'l_phau', 'l_sgbs', 's_csgold', 's_zgldus', 's_sgld', 's_xgld'] ,
"value" : [1289, 1289, 1289, 1289, 1289, 1280, 1279, 1279, 1005, 680]
})
exsymbol_df.head()


# # matplotlib
# here we get a overview of the amount and close in the same graph during the time interval

# In[18]:


df.plot.line(x='datetime', y=['close', 'amount'])

