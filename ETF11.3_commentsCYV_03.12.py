#!/usr/bin/env python
# coding: utf-8

# In[87]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


# In[88]:


df = pd.read_csv('/Users/lobe/Desktop/OneDrive/merged_goldeikon-5y-1D-10symbols-20210207.csv')
df.head() #good way to see a glimpse of the dataset


# In[94]:

# What do you use this fuction for?
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df)


# # Describe dataset

# In[16]:


df.describe() 


# In[21]:


df.describe(include=[np.object])


# In[23]:


df.describe(include='all')


# In[ ]:





# In[ ]:





# # Datetime

# In[ ]:


# You can check min and max datetime, its important to have the date range correctly when we analyze information.
# check min and max datetime with describe function


# In[19]:


x = datetime.datetime.now()
print(x)


# In[20]:


date_object = datetime.date.today()
print(date_object)


# In[ ]:





# In[ ]:





# # ETF

# In[97]:


#Also good to see aggregated info, dont forget per ETF.
#Describe aggregated info per ETF.
#Describe function shows aggregated info


# In[ ]:





# In[46]:


df['ex_symbol'].unique() # good one, it's key to verify that we have what we need, sometimes
# we get datasets that contain other ETF that are not relevant for our analysis.


# In[85]:


df['ex_symbol'].nunique() # I didnt know about that method, i usually use len() to calculate the number of unique ETFs


# In[34]:


df["ex_symbol"].value_counts()


# In[45]:


df["ex_symbol"].describe()


# In[54]:


s = pd.Series(['l_sgld', 's_sgld', 'l_igln', 'l_xgld', 's_xgld', 'l_gbsx', 'l_phau', 's_csgold', 'l_sgbs', 's_zgldus'])
s.describe() # good, how they take "l_gbsx" as the top? 


# In[ ]:





# In[ ]:





# # List function

# In[102]:


etf_list =['l_sgld', 's_sgld', 'l_igln', 'l_xgld', 's_xgld', 'l_gbsx', 'l_phau', 's_csgold', 'l_sgbs', 's_zgldus']
print(etf_list)


# In[ ]:





# In[ ]:





# # Matplotlib

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Also there are some shortcuts that you might want to know like when you press B, it creates a new box below the one you're in.

# You can press **M** after that to select Markdown and have text in your jupyter lab as Im doing now.

# To activate edition of a block just *press enter*
