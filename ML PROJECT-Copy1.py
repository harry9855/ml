#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


# In[37]:


loan_dataset = pd.read_csv("C:\\Users\\hp\\Downloads\\train_u6lujuX_CVtuZ9i (1).csv")
loan_datasets =  pd.read_csv("C:\\Users\\hp\\Downloads\\loanML.csv")


# In[6]:


type(loan_dataset)


# In[38]:


loan_datasets.head()


# In[15]:


loan_dataset.shape


# In[16]:


loan_dataset.describe()


# In[17]:


# number of missing values in each column
loan_dataset.isnull().sum()


# In[7]:


loan_dataset = loan_dataset.dropna()
loan_datasets = loan_datasets.dropna()


# In[19]:


loan_dataset.isnull().sum()


# In[9]:


loan_dataset.replace({"Loan_Status":{'N':0,'Y':1}},inplace=True)

loan_datasets.replace({"Loan_Status":{'N':0,'Y':1}},inplace=True)


# In[22]:


loan_dataset.head()


# In[11]:


loan_dataset['Dependents'].value_counts()


# In[12]:


loan_datasets['Dependent'].value_counts()


# In[13]:


loan_dataset = loan_dataset.replace(to_replace='3+', value=4)
loan_datasets = loan_datasets.replace(to_replace='3+', value=4)


# In[25]:


loan_dataset['Dependents'].value_counts()


# In[29]:


sns.countplot(x='Education',hue='Loan_Status',data=loan_dataset)


# In[30]:


sns.countplot(x='Married',hue='Loan_Status',data=loan_dataset)


# In[41]:


loan_datasets.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},
                      'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)


# In[42]:


loan_dataset.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},
                      'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)


# In[17]:


loan_datasets.head()


# In[43]:


loan_dataset.head()


# In[52]:


X = loan_dataset.drop(columns=['Loan_ID','Loan_Status'],axis=1)
Y = loan_dataset['Loan_Status']

X1 = loan_datasets.drop(columns=['Loan_Id','Name','Loan_Status','IdProof','IdNumber','Loan_Type','ROI'],axis=1)
Y1 = loan_datasets['Loan_Status']
X2 = loan_datasets['Name']


# In[55]:


print(X2[0])


# In[25]:


X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=2)


# In[26]:


print(X.shape, X_train.shape, X_test.shape)


# In[27]:


classifier = svm.SVC(kernel='linear')


# In[28]:


classifier.fit(X_train,Y_train)


# In[31]:


X_train_prediction = classifier.predict(X_train)
training_data_accuray = accuracy_score(X_train_prediction,Y_train)


# In[32]:


print('Accuracy on training data : ', training_data_accuray)


# In[33]:


X_test_prediction = classifier.predict(X_test)
test_data_accuray = accuracy_score(X_test_prediction,Y_test)


# In[34]:


print('Accuracy on test data : ', test_data_accuray)


# In[48]:


prediction = classifier.predict(X1)
print(prediction)


# In[56]:


if prediction==1:
    print(X2[0],"will pay the loan")
else:
    print("He may default the loan")

