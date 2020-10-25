#!/usr/bin/env python
# coding: utf-8

# # FIFA Wordl Cup Analysis
# ## Python 3 and Jupyter Lab
# ### Anaconda
# By: Eng. Javier Blanco
# 10/25/2020

# Data Set downloaded from: https://www.kaggle.com/abecklas/fifa-world-cup
# 
# WorldCupMatches.csv was downloaded
# 
# 

# ## Importing libraries and tools

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Importing raw data and cleaning it
raw_matches_df = pd.read_csv('WorldCupMatches.csv')
raw_matches_df


# In[3]:


#Knowing how many rows and columns has this dataset
raw_matches_df.shape


# In[4]:


#learn list of column names
raw_matches_df.columns


# In[5]:


# getting information summarized of data. Also, it guves information
#about columns, number of no-nulls values in each column, and so on. 

raw_matches_df.info()


# In[6]:


#I will remove information abou Referee and assistants, to do so, I use drop pandas function
matches_df = raw_matches_df.drop(['Referee', 'Assistant 1', 'Assistant 2'], axis=1)
matches_df


# In[7]:


#Removing NaN data
matches_df = matches_df.dropna()
matches_df.shape


# ## Exploratory Analysis

# This method involves performing operations on dataset in order to understand the data and learn potential patterns. Basically it helps us make sense of the data we have.

# In[8]:


# Number od matches and teams
#we can use "groupby" function of Pandas and get macthes by Worldcup season
matches_per_season = matches_df.groupby('Year').MatchID.count()
matches_per_season


# In[9]:


#we can plot a bar graph by using seaborn and matplotlib. 
#Some features must be adjusted at first
sns.set_style('darkgrid')
plt.rcParams['font.size'] = 14
plt.rcParams['figure.figsize'] = (9, 5)
plt.rcParams['figure.facecolor'] = '#00000000'


# In[10]:


plt.figure(figsize=(12,6))
plt.xticks(rotation=60)
plt.title("Matches per Year")
matches_per_season_plot = sns.barplot(
                                    x=matches_per_season.index,
                                    y=matches_per_season)
matches_per_season_plot.set(xlabel="Year", ylabel= 'Nº of Macthes')


# In[11]:


#Wins an Winners
#filter1 = (matches_df.win_by_year == 0) & (matches_df.result=='normal')


# In[12]:


#naming teams
matches_df = matches_df.rename(columns={'Home Team Name':'Winner', 'Away Team Name': 'Loser'})
matches_df


# In[14]:


total_matches_played = (matches_df.Winner.value_counts() +
                       matches_df.Loser.value_counts()).sort_values(ascending = False)


# In[17]:


total_matches_played=total_matches_played.dropna()
total_matches_played


# In[18]:


#graphically
df_matches_played = total_matches_played.head(20)
plt.figure(figsize=(15,12))
plt.title('Total matches played by country')
total_macthes_played_plot = sns.barplot(y=df_matches_played.index,
                                        x=df_matches_played)
total_macthes_played_plot.set(ylabel='Country/Team', xlabel = 'Matches');


# In[19]:


#Legacy by calculating most wins
most_wins = matches_df.Winner.value_counts()
most_wins


# In[20]:


win_percen = (most_wins / total_matches_played).sort_values(ascending = False)*100
win_percen


# ## Which are the most and least consistent teams across all seasons?

# In[21]:


# Created a data frame between different values of winner and season using pd.crosstab().
#Plotted the data frame as a heatmap.
won_each_match = pd.crosstab(matches_df['Winner'], matches_df['Year'])
won_each_match


# In[22]:


plt.figure(figsize=(20,20))
plt.xlabel('Year')
plt.ylabel('Team')
plt.title('Matches won each year')
sns.heatmap(won_each_match, annot = True, cmap = 'rocket_r', fmt='d',
                           cbar_kws={"orientation": "horizontal"});


# In[30]:


best_ones = won_each_match.loc[['Brazil', 'Argentina', 'Uruguay','Germany', 'Spain']]
best_ones


# In[31]:


plt.figure(figsize=(18,12))
plt.xlabel('Year')
plt.ylabel('Team')
plt.title('Matches won each year')
sns.heatmap(best_ones, annot = True, cmap = 'rocket_r', fmt='d',
                           cbar_kws={"orientation": "horizontal"});

