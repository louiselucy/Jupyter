#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import datetime
import itertools
from itertools import groupby


# In[24]:


df = pd.read_csv('/Users/lucy/Documents/Vinter/merged_goldeikon.csv')
df.head(5) 


# In[45]:


df.tail(5)


# # Describe dataset 
# Here we get a overview of the data set.

# In[25]:


df.describe() 


# In[26]:


df.describe(include=[np.object])


# In[27]:


df.describe(include='all')


# # Datetime

# In[28]:


x = datetime.datetime.now()
print(x)


# In[29]:


date_object = datetime.date.today()
print(date_object)


# In[37]:


df['datetime'] = pd.to_datetime(df['datetime'])


# In[38]:


df.groupby(['ex_symbol', 'datetime']).mean()


# In[39]:


df['datetime'] = pd.to_datetime(df['datetime'])
df.info()


# In[ ]:





# In[ ]:





# # exchange traded fund (ETF) 
# #here we can see the diffrent names of etf's and it's values

# In[32]:


df['ex_symbol'].unique() 


# In[12]:


df['ex_symbol'].nunique() 


# In[13]:


df["ex_symbol"].describe()


# In[14]:


s = pd.Series(['l_sgld', 's_sgld', 'l_igln', 'l_xgld', 's_xgld', 'l_gbsx', 'l_phau', 's_csgold', 'l_sgbs', 's_zgldus'])
s.describe() 


# In[15]:


df["ex_symbol"].value_counts()


# In[18]:


exsymbol_df = pd.DataFrame( {     
"exsymbol" : ['l_gbsx', 'l_xgld', 'l_igln', 'l_sgld', 'l_phau', 'l_sgbs', 's_csgold', 's_zgldus', 's_sgld', 's_xgld'] ,
"value" : [1289, 1289, 1289, 1289, 1289, 1280, 1279, 1279, 1005, 680]})
df.groupby(['exsymbol']).sum()
exsymbol_df.head()


# In[41]:


exsymbol_df.plot.line()


# In[46]:


exsymbol_df.plot.hist()


# # Matplotlib histogram and linechart

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[134]:


df.plot.line(x ='ex_symbol', y ='amount')


# In[33]:


df.plot.hist(x ='ex_symbol', y ='amount')


# In[51]:


df.plot.scatter(x ='datetime', y ='amount')


# In[135]:


data.plot.line(x ='datetime', y ='amount')


# In[136]:


fig = px.line(df, x = 'datetime', y = 'amount', title='Amount / Time')
fig.show()


# In[137]:


fig = px.histogram(df, x = 'ex_symbol', y = 'amount', title='Exchange Amount')
fig.show()



#MESSAGE
#Can add files like this, updates versions, can invite you to see the code in colab. Have not got an githu version for jupyterlab.
#will move over to jupyterlab now.


# Also there are some shortcuts that you might want to know like when you press B, it creates a new box below the one you're in.

# You can press **M** after that to select Markdown and have text in your jupyter lab as Im doing now.

# To activate edition of a block just *press enter*



