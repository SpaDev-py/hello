#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
#df = pd.read_csv("weather.csv")
weather_data = {
    'data': ['1/1/2020', '1/2/2020','1/3/2020', '1/4/2020', '1/5/2020', '1/6/2020'],
    'temperature' : [32,35,28,24,32,31],
    'windspeed' : [6,7,2,7,4,2],
    'events' : ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
}
df = pd.DataFrame(weather_data)


# In[10]:


df.head()


# In[11]:


df[1:]


# In[12]:


df[1:5:2]


# In[13]:


#def df[0] just an error


# In[15]:


df


# In[16]:


rows, columns = df.shape


# In[17]:


rows


# In[18]:


columns


# In[19]:


babbs, midas = df.shape


# In[20]:


babbs


# In[21]:


midas


# In[22]:


rows, columns = df.shape


# In[23]:


rows


# In[24]:


columns


# In[25]:


df.columns


# In[27]:


df.temparature


# In[29]:


df.data


# In[30]:


df.events   # or df['events']  in form of accessing a python dict.


# In[32]:


df


# In[34]:


type(df)  #or type(df['event'])


# In[37]:


df


# In[36]:


df[['events','data']]


# In[39]:


df['temparature']


# In[40]:


df['temparature'].max()


# In[42]:


df['temparature'].mean()   #for the average value


# In[49]:


def add(nums):
    count = 0
    for i in nums:
        count = count + i
    print(count)

x = df['temparature']
add(df['temparature'])  
#or assign df['temparature'] to a var then use add(<var>)


# In[51]:


df


# In[54]:


df.describe()


# In[55]:


#conditions in the dataframe

df[df.temparature >= 32]

#this directly translates as: return all the temps higher than 32


# In[57]:


df[df.temparature == df.temparature.max()]  #or == df['temparature'].max(). this is best for when the name of the data contains spaces e.g 'wind speed'

#returns the row of the highest temperature


# In[65]:


#to perfom the same action but this time not print the entire row, just a particular one

df['data'][df.temparature == df.temparature.max()]

#can also print multiple data
df[['data','temparature']][df.temparature == df.temparature.max()]
#notice only the second code is run, the second assignment for df overwrites the first


# In[66]:


df


# In[67]:


df.index

#a function to return the index of the dataset


# In[68]:


df.set_index('data')

#a method to set the index column of the data set to something else. in this case the data column is used as the index
#TO USE THE OUTCOME OF THIS METHOD U NEED TO SAVE IT BY USING
#df.set_index('data', inplace = True)


# In[69]:


df


# In[70]:


df.set_index('data', inplace = True)


# In[71]:


df


# In[72]:


#after saving, this is easier to search a data by date by passing into the .loc() parameter

df.loc['1/4/2020']

#also if the loc value appears more than once in the index, it returns all possible results


# In[73]:


#to reset to its initial state

df.reset_index(inplace = True)


# In[74]:


df


# In[76]:


df


# In[ ]:




