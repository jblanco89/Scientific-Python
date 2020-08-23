#!/usr/bin/env python
# coding: utf-8

# ## Cryptocurrencies Analysis using alpha vantage library
# #### Performing market behaviour with graphic analysis
# 
# By Eng. Javier Blanco

# In[1]:


# Do not forget to install alpha vantage dependency
#pip install alpha-vantage 


# ### Importing packages

# In[2]:


import pandas as pd
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt


# #### Get api key by accessing to 'https://www.alphavantage.co/support/#api-key'

# In[3]:


# Api key given
api_key = '9YUGBQ4SDSM881A2'


# In[4]:


btc = CryptoCurrencies(key=api_key, output_format='pandas')
data_btc, meta_data_btc = btc.get_digital_currency_daily(symbol='BTC', market='CNY')

eth = CryptoCurrencies(key=api_key,output_format='pandas')
data_eth, meta_data_eth = eth.get_digital_currency_daily(symbol='ETH', market='CNY')


# In[5]:


df1 = data_btc['4b. close (USD)']
df2 = data_eth['4b. close (USD)']

total_df = pd.concat([df1, df2], axis=1)
print(total_df)


# In[6]:


figure, axis_1 = plt.subplots()
axis_1 = df1.plot(figsize=(15,8))
plt.xlabel("Date")
plt.ylabel("Price BTC-USD")
axis_2 = axis_1.twinx()
axis_2= df2.plot(figsize=(15,8), color='black')
plt.xlabel("Date")
plt.ylabel("Price ETH-USD")
plt.title('Bitcoin (BTC) and Etherum (ETH) daily close values')
plt.grid()
plt.show()


# In[ ]:




