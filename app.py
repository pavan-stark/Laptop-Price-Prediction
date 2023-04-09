import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import streamlit as st

# load the data
df = pd.read_csv('laptop.csv')

# extract the features and target variable
X = df[['RAM Capacity', 'RAM Type', 'Storage_Capacity', 'Storage_Type', 'CPU Processor']]
y = df['MRP']

# preprocess categorical features using one-hot encoding
ct = ColumnTransformer([('encoder', OneHotEncoder(), [1, 3, 4])], remainder='passthrough')
X = ct.fit_transform(X)

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create a linear regression model and fit it to the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Define a function to run the app
def run_app():
    st.title('Laptop Price Predictor')

    # create a form to get user input
    ram_capacity = st.selectbox('RAM Type', ['8','4','16','32'])
    ram_type = st.selectbox('RAM Type', df['RAM Type'].unique())
    storage_capacity = st.selectbox('Storage Capacity', ['512','128','256','1000','2000'])
    storage_type = st.selectbox('Storage Type', ['HDD', 'SSD'])
    cpu_processor = st.selectbox('CPU Processor', df['CPU Processor'].unique())

    # preprocess the user input using the same ColumnTransformer as before
    user_data = pd.DataFrame({'RAM Capacity': [ram_capacity], 'RAM Type': [ram_type], 'Storage_Capacity': [storage_capacity], 'Storage_Type': [storage_type], 'CPU Processor': [cpu_processor]})
    user_data = ct.transform(user_data)

    # use the model to make a prediction on the user input
    predicted_price = model.predict(user_data)

    st.write(f"Predicted Price: ${predicted_price[0]:,.2f}")

if __name__ == '__main__':
    run_app()
