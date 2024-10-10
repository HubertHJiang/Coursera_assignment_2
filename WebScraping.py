# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:27:15 2024

@author: 27519
"""
## 1 Tesla Stock Data Using yfinance
import yfinance as yf
import pandas as pd

# 创建特斯拉股票的ticker对象
tesla = yf.Ticker("TSLA")

# 使用ticker对象和history函数提取股票信息，并保存在名为tesla_data的dataframe中
tesla_data = tesla.history(period="max")

# 重置索引，保存，并显示tesla_data dataframe的前五行
tesla_data.reset_index(inplace=True)
print(tesla_data.head())



## 2 Tesla Revenue Data Using Webscraping
import requests
from bs4 import BeautifulSoup

# 特斯拉财务报告的URL，这里需要替换为实际的URL
url = 'https://backlinko.com/tesla-stats'

# 发送HTTP请求
response = requests.get(url)

# 解析HTML内容
soup = BeautifulSoup(response.text, 'html.parser')

# 根据实际的HTML结构提取收入数据，这里需要根据实际情况调整
# 收入数据在一个表格中
revenue_table = soup.find('table', {'class': 'revenue-table'})
revenue_data = pd.read_html(str(revenue_table))[0]

# 打印提取的数据
print(revenue_data.head())



## 3 Tesla Stock and Revenue Dashboard
import streamlit as st
import pandas as pd
import yfinance as yf

# 创建特斯拉股票的ticker对象
tesla = yf.Ticker("TSLA")

# 提取股票信息
tesla_data = tesla.history(period="max")

# 特斯拉的收入数据
tesla_revenue_data = pd.read_csv('tesla_revenue_data.csv')

# 在Streamlit中创建仪表板
st.title('特斯拉股票和收入仪表板')

# 显示股票数据
st.subheader('特斯拉股票数据')
st.write(tesla_data.head())

# 显示收入数据
st.subheader('特斯拉收入数据')
st.write(tesla_revenue_data.head())