# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# %%
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv', encoding= 'unicode_escape')

# %%
df.shape

# %% [markdown]
# There are 1470 rows and 35 columns in the dataset.

# %%
df.head()

# %%
df.info()

# %%
pd.isnull(df)

# %%
pd.isnull(df).sum()

# %% [markdown]
# There are no null values in the dataset.

# %%
df.columns

# %%
df.describe()

# %%
df.dtypes

# %%
for column in df.columns:
    unique_values = df[column].nunique()
    print(f"{column}: {unique_values} unique values")

# %% [markdown]
# <h4>Data Encoding</h4>

# %%
df['Attrition'].unique()

# %%
df['Attrition']=df['Attrition'].map({'Yes': 1, 'No':0})

# %%
df['BusinessTravel'].unique()

# %%
df['BusinessTravel']=df['BusinessTravel'].map({'Non-Travel': 0, 'Travel_Rarely':1, 'Travel_Frequently':2})

# %%
df['Department'].unique()

# %%
df['Department']=df['Department'].map({'Sales':0, 'Research & Development':1, 'Human Resources':2})

# %%
df['EducationField'].unique()

# %%
df['EducationField']=df['EducationField'].map({'Life Sciences':0, 'Medical':1, 'Marketing':2, 'Technical Degree':3, 'Human Resources':4, 'Other':5})

# %%
df['Gender'].unique()

# %%
df['Gender']=df['Gender'].map({'Male':0, 'Female':1})

# %%
df['MaritalStatus'].unique()

# %%
df['MaritalStatus']=df['MaritalStatus'].map({'Divorced':0, 'Single':1, 'Married':2})

# %%
df['Over18'].unique()

# %%
df['Over18']=df['Over18'].map({'Y':0})

# %%
df['OverTime'].unique()

# %%
df['OverTime']=df['OverTime'].map({'No':0, 'Yes':1})

# %% [markdown]
# <h2>Exploratory Data Analysis</h2>

# %%
sns.countplot(data = df, x = 'BusinessTravel', hue = 'Attrition')

# %%
sns.countplot(data = df, x = 'Department', hue = 'Attrition')

# %%
sns.countplot(data = df, x = 'EducationField', hue = 'Attrition')

# %%
sns.countplot(data = df, x = 'Gender', hue = 'Attrition')

# %%
sns.countplot(data = df, x = 'MaritalStatus', hue = 'Attrition')

# %%
sns.countplot(data = df, x = 'Over18', hue = 'Attrition')

# %%
sns.countplot(data = df, x = 'OverTime', hue = 'Attrition')

# %%



