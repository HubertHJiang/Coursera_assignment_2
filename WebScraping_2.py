# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:30:01 2024

@author: 27519
"""

##1 Extracting GameStop Stock Data Using yfinance
import yfinance as yf
import pandas as pd

# 创建GameStop股票的ticker对象
gamestop = yf.Ticker("GME")

# 使用ticker对象和history函数提取股票信息，并保存在名为gamestop_data的dataframe中
gamestop_data = gamestop.history(period="max")

# 重置索引，保存，并显示gamestop_data dataframe的前五行
gamestop_data.reset_index(inplace=True)
print(gamestop_data.head())



##2 Extracting GameStop Revenue Data Using Webscraping
import requests
from bs4 import BeautifulSoup

# GameStop财务报告的URL，这里需要替换为实际的URL
url = 'https://finbox.com/NYSE:GME/explorer/total_rev/'

# 发送HTTP请求
response = requests.get(url)

# 解析HTML内容
soup = BeautifulSoup(response.text, 'html.parser')

# 提取收入数据，这里需要根据实际情况调整
revenue_table = soup.find('table', {'class': 'GameStop Corp Revenue Benchmarks'})
revenue_data = pd.read_html(str(revenue_table))[0]

# 打印提取的数据
print(revenue_data.head())



##3 GameStop Stock and Revenue Dashboard
import streamlit as st
import pandas as pd
import yfinance as yf

# 创建GameStop股票的ticker对象
gamestop = yf.Ticker("GME")

# 提取股票信息
gamestop_data = gamestop.history(period="max")

# 假设你已经有了GameStop的收入数据
# gamestop_revenue_data = pd.read_csv('gamestop_revenue_data.csv')

# 在Streamlit中创建仪表板
st.title('GameStop股票和收入仪表板')

# 显示股票数据
st.subheader('GameStop股票数据')
st.write(gamestop_data.head())

# 显示收入数据
st.subheader('GameStop收入数据')
# st.write(gamestop_revenue_data.head())