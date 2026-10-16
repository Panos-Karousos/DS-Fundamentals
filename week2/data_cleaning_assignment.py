#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[3]:


df = pd.read_csv("dirty_data_sample.csv")
df


# In[21]:


df.duplicated()


# In[5]:


df.describe(include="all")


# In[6]:


df.isnull().sum()


# In[7]:


df.dtypes


# In[8]:


df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df.dtypes


# In[10]:


df["Age"] = df["Age"].fillna(df["Age"].median())
df["Income"] = df["Income"].fillna(df["Income"].median())
df["Name"] = df["Name"].fillna("Unknown")
df["City"] = df["City"].fillna("Unknown")
df = df.drop_duplicates()


# In[11]:


df


# In[12]:


df.isnull().sum()


# In[13]:


df.dtypes


# In[14]:


df.duplicated().sum()


# In[15]:


df.info()
df.describe(include="all")
