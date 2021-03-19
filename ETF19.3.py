#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import datetime
import itertools
from itertools import groupby


# In[59]:


df = pd.read_csv('/Users/lucy/Documents/Vinter/merged_goldeikon.csv')
df.head() 


# # Describe dataset 
# Here we get a overview of the data set.

# In[62]:


df.describe() 


# In[63]:


df.describe(include=[np.object])


# In[64]:


df.describe(include='all')


# # Datetime

# In[65]:


x = datetime.datetime.now()
print(x)


# In[66]:


date_object = datetime.date.today()
print(date_object)


# In[67]:


df['datetime'] = pd.to_datetime(df['datetime'])


# In[68]:


df.groupby(['ex_symbol', 'datetime']).mean()


# # exchange traded fund (ETF) 
# #here we can see the diffrent names of etf's and the values

# In[69]:


df['ex_symbol'].unique() 


# In[70]:


df['ex_symbol'].nunique() 


# In[71]:


df["ex_symbol"].describe()


# In[72]:


s = pd.Series(['l_sgld', 's_sgld', 'l_igln', 'l_xgld', 's_xgld', 'l_gbsx', 'l_phau', 's_csgold', 'l_sgbs', 's_zgldus'])
s.describe() 


# In[73]:


df["ex_symbol"].value_counts()


# In[85]:


df = pd.DataFrame( {     
"exsymbol" : ['l_gbsx', 'l_xgld', 'l_igln', 'l_sgld', 'l_phau', 'l_sgbs', 's_csgold', 's_zgldus', 's_sgld', 's_xgld'] ,
"value" : [1289, 1289, 1289, 1289, 1289, 1280, 1279, 1279, 1005, 680]})
df.groupby(['exsymbol']).sum()
df


# In[ ]:





# # Matplotlib histogram and linechart

# In[134]:


df.plot.line(x ='ex_symbol', y ='amount')


# In[135]:


data.plot.line(x ='datetime', y ='amount')


# In[136]:


fig = px.line(df, x = 'datetime', y = 'amount', title='Amount / Time')
fig.show()


# In[137]:


fig = px.histogram(df, x = 'ex_symbol', y = 'amount', title='Exchange Amount')
fig.show()


# Also there are some shortcuts that you might want to know like when you press B, it creates a new box below the one you're in.

# You can press **M** after that to select Markdown and have text in your jupyter lab as Im doing now.

# To activate edition of a block just *press enter*
