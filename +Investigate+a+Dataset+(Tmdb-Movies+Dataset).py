
# coding: utf-8

# # Investigate a Dataset (Tmdb-Movies Dataset)

# # AMR SAAD MAHMOUD

# Table of Contents¶
# 
# I-ntroduction
# 
# 2-Data Wrangling
# 
# 3-Exploratory Data Analysis
# 
# 4-Conclusions
# 
# 
# 

# # 1-introduction

# dataset Contain:
# 
# Total Rows = 10866
# 
# Total Columns = 21
# 
# After Seeing the dataset we can say that some columns is contain null values

# Questions answered by the dataset
# 
# Which year has the highest release of movies?
# 
# Which Movie Has The Highest Or Lowest Profit? Top 10 movies which earn highest profit?
# 
# Movie with Highest And Lowest Budget?
# 
# Which movie made the highest revenue and lowest as well?
# 
# Movie with shorest and longest runtime?
# 
# Which movie get the highest or lowest votes (Ratings).
# 
# Which Year Has The Highest Profit Rate?
# 
# Which length movies most liked by the audiences according to their popularity?
# 
# Average Runtime Of Movies From Year To Year?
# 
# How Does The Revenue And Popularity differs Budget And Runtime? And How Does Popularity Depends On Profit?
# 
# Which Month Released Highest Number Of Movies In All Of The Years? And Which Month Made The Highest Average Revenue?
# 
# Which Genre Has The Highest Release Of Movies?
# 
# Which genres are most popular from year to year?
# 
# Most Frequent star cast?
# 
# Top 20 Production Companies With Higher Number Of Release?
# 
# Life Time Profit Earn By Each Production Company?
# 
# Top 20 Director Who Directs Maximum Movies?
# 
# What kinds of properties are associated with movies that have high revenues?
# 

# In[3]:

#import packedg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().magic('matplotlib inline')


# # 2-Data Wrangling

# In[4]:

#import dataset
df=pd.read_csv("C:/Users/amr/Desktop/tmdb_movies_data.csv")
df.head(5)


# In[7]:

df.tail(5)


# In[5]:

df.info()


# In[6]:

df.describe()


# In[8]:

df.isnull().sum()


# Data Cleaning (Removing The Unused Information From The Dataset)
# 
# Information That We Need To Delete Or Modify
# 
# We need to remove duplicate rows from the dataset
# 
# Changing format of release date into datetime format
# 
# Remove the unused colums that are not needes in the analysis process.
# 
# Remove the movies which are having zero value of budget and revenue

# In[10]:

#remove duplicate rows from the dataset
df.duplicated().sum()


# In[11]:

#code
df.drop_duplicates(inplace=True)


# In[12]:

#test
df.duplicated().sum()


# In[13]:

#Changing format of release date into datetime format
#code
df.release_date=pd.to_datetime(df.release_date)


# In[14]:

#test
df.release_date.head(5)


# In[15]:

#Remove the unused colums that are not needes in the analysis process

#code
df.drop(['budget_adj','revenue_adj','overview','imdb_id','homepage','tagline'],axis =1,inplace = True)


# In[16]:

#test
df.head(5)


# In[23]:

#Remove the movies which are having zero value of budget and revenue

#code
zero_list=['budget','revenue']
df[zero_list]=df[zero_list].replace(0,np.nan)
df.dropna(subset=zero_list,inplace=True)


# In[25]:

#test
df[df['budget']==0]


# # 3-Exploratory Data Analysis

# # question one
# #Which year has the highest release of movies?

# In[41]:

#code
high_year=df.groupby('release_year').count()['id']
print(data.tail())

plt.xlabel("release_year")
plt.ylabel("number of movie")
plt.plot(high_year)


# In[40]:

high_year.idxmax()


# # Research Question 2 : Which Movie Has The Highest Or Lowest Profit?

# In[43]:

df['profit']=df['revenue']-df['budget']
df.head(2)


# In[48]:

#method one 
print(df.profit.max())
print(df.profit.min())


# In[45]:

df[df['profit']==2544505847.0]


# In[49]:

df[df['profit']==-413912431.0]


# In[50]:

#method two
def high_mini(colomn):
    high_index=df[colomn].idxmax()
    mini_index=df[colomn].idxmin()
    high=pd.DataFrame(df.loc[high_index,:])
    low=pd.DataFrame(df.loc[mini_index,:])
    
    return high,low;

print(high_mini('profit'))



# # Movie with Highest And Lowest Budget?

# In[59]:

print(high_mini('budget'))


# # Which movie made the highest revenue and lowest as well?

# In[60]:

print(high_mini('revenue'))


# In[62]:

df['runtime']=df['runtime'].replace(0,np.nan)


# # Movie with shorest and longest runtime?

# In[63]:

print(high_mini('runtime'))


# # Which movie get the highest or lowest votes (Ratings)

# In[67]:

print(high_mini('vote_average'))


# # Which Year Has The Highest Profit Rate?

# In[71]:

year_profit=df.groupby('release_year')['profit'].sum()
plt.plot(year_profit)


# In[72]:

year_profit.idxmax()


# # Which length movies most liked by the audiences according to their popularity?

# In[74]:

lenght_runtime=df.groupby('runtime')['popularity'].sum()
plt.plot(lenght_runtime)


# According to the plot we can say that movies in the range of 100-200 runtime are more popular than other runtime movies. Because it is boring to see the long duration movies

# # Average Runtime Of Movies From Year To Year?

# In[79]:

runtime_year=df.groupby('release_year')['runtime'].mean()
plt.plot(runtime_year)

