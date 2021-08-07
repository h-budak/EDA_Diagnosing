#!/usr/bin/env python
# coding: utf-8

# # How certain diagnostic factors affect the diabetes outcome of women patients
# Inspecting, cleaning, and validating the data.
# Columns
# Pregnancies: Number of times pregnant
# Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
# BloodPressure: Diastolic blood pressure
# SkinThickness: Triceps skinfold thickness
# Insulin: 2-Hour serum insulin
# BMI: Body mass index
# DiabetesPedigreeFunction: Diabetes pedigree function
# Age: Age (years)
# Outcome: Class variable (0 or 1)

# In[3]:


import pandas as pd
import numpy as np


# In[5]:


# Load the data in a variable called diabetes_data and print the first few rows.
diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())


# In[6]:


#How many columns
print(len(diabetes_data.columns))


# In[7]:


#How many rows
print(len(diabetes_data))


# In[8]:


#null values
print(diabetes_data.isnull().sum())


# In[9]:


print(diabetes_data.info())


# In[10]:


#summary statistics on diabates_data using the .describe() method.
print(diabetes_data.describe())


# In[12]:


#to replace the instances of 0 with NaN in the five columns
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)


# In[13]:


#check null values
print(diabetes_data.isnull().sum())


# In[14]:


#all of the rows that contain missing (null) values
print(diabetes_data[diabetes_data.isnull().any(axis=1)])


# In[15]:


#data types of each column in diabetes_data
print(diabetes_data.dtypes)


# In[18]:


print(diabetes_data.Outcome.unique())
diabetes_data[['Outcome']] = diabetes_data[['Outcome']].replace('O',0)


# In[ ]:




