#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel('C:\\Users\\Saqlain Bakshabhaiji\\Desktop\\running\\data.xlsx')


# In[3]:


df


# In[4]:


df.isna().sum()


# In[5]:


df = df.dropna()
df['Gender'] = df['Gender'].astype('category')
df['Gender'] = df['Gender'].cat.codes
df = df.dropna()
df['average study hours'] = df['average study hours'].astype('category')
df['average study hours'] = df['average study hours'].cat.codes
df['average screen time'] = df['average screen time'].astype('category')
df['average screen time'] = df['average screen time'].cat.codes
df['participation'] = df['participation'].astype('category')
df['participation'] = df['participation'].cat.codes
df.rename(columns={
    'participation': 'participation(out of five)',
    'extra curricular participation': 'extra curricular participation(out of five)',
    'timely submission': 'timely submission(out of five)',
    'parents involvement': 'parents involvement(out of five)',
    'time management': 'time management(out of five)',
    'interest': 'interest(out of five)'
}, inplace=True)


# In[6]:


x = df.drop(columns = ['Timestamp','Full Name','sources','above 70?','extra curriculur','previous percenatage'])
y = df['previous percenatage']                  


# In[7]:


from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)


# In[8]:


from sklearn.preprocessing import StandardScaler


# In[9]:


scaler = StandardScaler()


# In[10]:


x_train_scaled = scaler.fit_transform(x_train)


# In[11]:


x_test_scaled = scaler.fit_transform(x_test)


# In[12]:


from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor()
rfr.fit(x_train_scaled,y_train)


# In[13]:


y_pred = rfr.predict(x_test_scaled)


# In[14]:


from sklearn.metrics import mean_squared_error


# In[15]:


rfr.score(x_train_scaled,y_train)


# In[16]:


#save the model
import joblib


# In[17]:


joblib.dump(rfr,'mark_prediction_final.model')


# In[18]:


model = joblib.load('mark_prediction_final.model')


# In[19]:


import pandas as pd
data_new = pd.DataFrame({
    'Gender':1,
    'last to last percentage':87,
    'average study hours':5,
    'average screen time':2,
    'attendance':90,
    'participation(out of five)':4,
    'extra curriculur participation':3,
    'timely submission(out of five)':5,
    'parents involvment':3,
    'time management(out of five)':4,
    'interest(out of five)':4,
    
},index=[0])


# In[20]:


model.predict(data_new)


# In[ ]:





# In[ ]:




