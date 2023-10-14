#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("C:/Users/hp/Desktop/11.abc.csv")
df


# In[2]:


cards_approved_by_states = df.groupby('State')['Aadhaar generated'].sum()
cards_approved_by_states


# In[3]:


cards_enrolment_rejected_by_states = df.groupby('State')['Enrolment Rejected'].sum()
cards_enrolment_rejected_by_states


# In[5]:


cards_approved_by_districts = df.groupby('District')['Aadhaar generated'].sum()
cards_approved_by_districts


# In[6]:


cards_rejected_by_districts = df.groupby('District')['Enrolment Rejected'].sum()
cards_rejected_by_districts


# In[7]:


gender_count = df['Gender'].value_counts()
gender_count


# In[9]:


age_counts = pd.cut(df['Age'],bins=[0,25,35,float("inf")],labels=['<25','25-35','>45']).value_counts()
age_counts

