import pandas as pd
import streamlit as st
import numpy as np
from matplotlib import image
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import os

st.title('Flipkart Laptop EDA')

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "flipkart.png")

DATA_PATH = os.path.join(dir_of_interest, "data", "laptop.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

data = pd.read_csv(DATA_PATH)
st.dataframe(data)

st.header('Columns of Data Frame')
st.write(data.columns)
st.header('Summary')
st.write(data.describe())

st.header('Types Of Processors')
st.bar_chart(data['CPU Processor'].value_counts())

st.header('Types Of Brand')
st.bar_chart(data['Brand'].value_counts())

st.header('Types Of Processor Brands')
st.bar_chart(data['CPU Brand'].value_counts())

st.header('Relationship between Storage Capacity and MRP')

# create the bar plot
fig, ax = plt.subplots()
sns.barplot(x=data['Storage_Capacity'], y=data['MRP'], ax=ax)
plt.xticks(rotation='vertical')

# display the plot in Streamlit
st.pyplot(fig)

st.header('Relationship between Storage Type and MRP')

# create the bar plot
fig, ax = plt.subplots()
sns.barplot(x=data['Storage_Type'], y=data['MRP'], ax=ax)
plt.xticks(rotation='vertical')

# display the plot in Streamlit
st.pyplot(fig)

st.header('Relationship between RAM Type and MRP')

# create the bar plot
fig, ax = plt.subplots()
sns.barplot(x=data['RAM Type'], y=data['MRP'], ax=ax)
plt.xticks(rotation='vertical')

# display the plot in Streamlit
st.pyplot(fig)

st.header('Relationship between RAM Capacity and MRP')

# create the bar plot
fig, ax = plt.subplots()
sns.barplot(x=data['RAM Capacity'], y=data['MRP'], ax=ax)
plt.xticks(rotation='vertical')

# display the plot in Streamlit
st.pyplot(fig)
