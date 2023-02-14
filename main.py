# Imports required ---
import streamlit as st
import sqlite3 as sqlite
import pandas as pd

@st.cache_data
def get_data():
  con = sqlite.connect("Fake_sales_data.db")
  data = pd.read_sql_query("SELECT * from SalesA", con)
  return data
data = get_data()


with st.expander("Welcome to the Streamlit Tour! 🎈 About this App"):
    st.write("""
         This app will introduce you to the Streamlit Library which
         helps to build and deploy data driven web apps with ease using Python. 😉
     """)
st.title('Sales Dashboard')
st.write(f"We have {len(data)} datapoints")

choice = st.selectbox("Select a Company", data["company"].unique(),index=0)

new_data = data[data["company"] == choice]

st.write(new_data.head())
# st.write(f"Sum of Sales {choice}:")
# st.write(new_data["price"].sum())

choice = st.multiselect("Select demographic", new_data["cat"].unique())
www = new_data["cat"].isin(choice)
new_dataa = new_data[www]
st.write(new_dataa.head())


# print the data / week
st.write(f"Sum of Sales per week {choice}:")
sumperweek = new_dataa.groupby(["week","cat"])["price"].sum()
st.write(sumperweek)


# plot sales through time
st.write(f"Sum of Sales {choice}:")
st.write(new_data["price"].sum())
st.line_chart(sumperweek,columns=['cat'])

# add a way to select demographic (young, active and retired)
#choice = st.selectbox("Select demographic", new_data["cat"].unique(),index=0)
#new_dataa = new_data[new_data["cat"] == choice]
#st.write(new_dataa.head())

