# streamlit run main.py     ---- to see web site

# Imports required ---
import streamlit as st
import time
import sqlite3 as sqlite
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Sales A",
    page_icon="✨"
)

with st.spinner('Wait for it...'):
    time.sleep(4)

@st.cache_data
def get_data():
  con = sqlite.connect("Fake_sales_data.db")
  data = pd.read_sql_query("SELECT * from SalesA", con)
  return data
data = get_data()

st.markdown("<h1 style='font-family: Gill Sans Semibold, sans-serif; text-align: center; color: #C26F4D;'>Sales Dashboard</h1>", unsafe_allow_html=True)
#st.title('Sales Dashboard')
st.write(f"We have {len(data)} datapoints")

choice = st.selectbox("Select a Company", data["company"].unique(),index=0)
new_data = data[data["company"] == choice]
st.write(new_data.groupby(["cat"])["price"].unique())

#st.write(new_data.head())

choicedemo = st.multiselect("Select demographic", new_data["cat"].unique())
www = new_data["cat"].isin(choicedemo)
new_dataa = new_data[www]

choiceprice = st.multiselect("Select price", new_dataa["price"].unique())
wwa = new_dataa["price"].isin(choiceprice)
new_data_price = new_dataa[wwa]

st.write(new_data_price.head())

#st.write(new_data.head())
# st.write(f"Sum of Sales {choice}:")
# st.write(new_data["price"].sum())

st.write(f"Volume of Sales {choice}:")
volum = new_data["price"].count()
st.write(volum)
# print the data / week
#-----st.write(f"Volume of Sales per week {choice}:")
sumperweek = new_data.groupby(["week"])["price"].count()

#st.write(sumperweek)
sumperweek = new_data.groupby(["week"])["price"].count().reset_index()

#revenue
st.write(f"Revenue of {choice}:")
revenue = new_data["price"].sum()
st.write(revenue)
sumperweekk = new_data.groupby(["week"])["price"].sum()

#st.write(sumperweek)
sumperweekk = new_data.groupby(["week"])["price"].sum().reset_index()

# plot volume & revenue through time

tab1, tab2 = st.tabs(["Volume", "Revenue"])

with tab1:
  figvol = px.line(sumperweek, x="week", y="price", title='Volume through time')
  st.plotly_chart(figvol)

with tab2:
  figrev = px.line(sumperweekk, x="week", y="price", title='Revenue through time')
  st.plotly_chart(figrev)