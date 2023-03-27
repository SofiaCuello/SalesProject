# streamlit run main.py     ---- to see web site

# Imports required ---
import streamlit as st
import time
import sqlite3 as sqlite
import pandas as pd
import plotly.express as px
st.set_page_config(
    page_title="Sales Dashboard ✨",
    page_icon="✨",
)
with st.spinner('Wait for it...'):
    time.sleep(4)
@st.cache_data
def get_data():
  con = sqlite.connect("Fake_sales_data.db")
  data = pd.read_sql_query("SELECT * from SalesA", con)
  return data
data = get_data()

def get_dataB():
  com = sqlite.connect("Fake_sales_data.db")
  datab = pd.read_sql_query("SELECT * from SalesB", com)
  return datab
datab = get_dataB()
st.markdown("<h1 style='font-family: Gill Sans Semibold, sans-serif; text-align: center; color: #332A28;'>Dashboard 📊 </h1>", unsafe_allow_html=True)
taba, tabb = st.tabs(["SalesA", "SalesB"])

with taba:
    st.markdown("<h1 style='font-family: Gill Sans Semibold, sans-serif; text-align: center; color: #C26F4D;'>SalesA</h1>", unsafe_allow_html=True)
    st.write(f"We have {len(data)} datapoints")
    
    choice = st.selectbox("Select a Company", data["company"].unique(),index=0)
    new_data = data[data["company"] == choice]
    st.write(new_data.groupby(["cat"])["price"].unique())
  
    choicedemo = st.multiselect("Select demographic", new_data["cat"].unique())
    www = new_data["cat"].isin(choicedemo)
    new_dataa = new_data[www]
    
    choiceprice = st.multiselect("Select price", new_dataa["price"].unique())
    wwa = new_dataa["price"].isin(choiceprice)
    new_data_price = new_dataa[wwa]
    st.write(new_data_price.head())
  
    #volume
    volum = new_data["price"].count()
    st.write(f"➙ Volume of Sales {choice}: **:red[{(volum)}] products sold**")
    sumperweek = new_data.groupby(["week"])["price"].count()
    sumperweek = new_data.groupby(["week"])["price"].count().reset_index()
    
  
    #revenue
    revenue = new_data["price"].sum()
    st.write(f"➙ Revenue of {choice}: **:red[$ {(revenue)}]**")    
    sumperweekk = new_data.groupby(["week"])["price"].sum()
    
    #st.write(sumperweek)
    sumperweekk = new_data.groupby(["week"])["price"].sum().reset_index()

    #Calculate market share for SalesA
    salesA_revenue = data['price'].sum()
    salesA_market_share = revenue / salesA_revenue * 100
    st.write(f"➙ Market Share of {choice}: **:red[{salesA_market_share:.2f}%]**")
    
    # calculate total volume and revenue for each company
    salesA_volum = data.groupby(["company"])["price"].count()
    salesA_reve = data.groupby(["company"])["price"].sum()
    salesA_market_share = data.groupby(["company"])["price"].sum() / salesA_revenue * 100
  
    tab1, tab2 = st.tabs(["Volume", "Revenue"])
    
    with tab1:
      figvol = px.line(sumperweek, x="week", y="price", title='Volume through time')
      st.plotly_chart(figvol)
    
    with tab2:
      figrev = px.line(sumperweekk, x="week", y="price", title='Revenue through time')
      st.plotly_chart(figrev)

    col1, col2, col3 = st.columns(3)

    with col1:        
        st.write("Volume for each company")
        st.write(salesA_volum)
      
    with col2:
        st.write("Revenue for each company")
        st.write(salesA_reve)
      
    with col3:
        st.write("Market Share for each company")    
        st.write(salesA_market_share)
        #st.write(f"{salesA_market_share:.2f}%")

with tabb:
    st.markdown("<h1 style='font-family: Gill Sans Semibold, sans-serif; text-align: center; color: #C26F4D;'>SalesB</h1>", unsafe_allow_html=True)
    st.write(f"We have {len(datab)} datapoints")
    choiceb = st.selectbox("Select a Company", datab["company"].unique(),index=0, key = "<uniquevalueofsomesort>")
    new_datab = datab[datab["company"] == choiceb]
    st.write(new_datab.groupby(["cat"])["price"].unique())
  
    choicedemob = st.multiselect("Select demographic", new_datab["cat"].unique(), key = "<uniquevalueofsomesor>")
    wwwb = new_datab["cat"].isin(choicedemob)
    new_dataab = new_datab[wwwb]
    
    choicepriceb = st.multiselect("Select price", new_dataab["price"].unique(), key = "<uniquevalueofsomeso>")
    wwab = new_dataab["price"].isin(choicepriceb)
    new_data_priceb = new_dataab[wwab]
    
    st.write(new_data_priceb.head())
    
    volumb = new_datab["price"].count()
    st.markdown(f"➙ Volume of Sales {choiceb}: **:red[{(volumb)}] products sold**")
    #st.write(volumb)
    sumperweekb = new_datab.groupby(["week"])["price"].count()
    sumperweekb = new_datab.groupby(["week"])["price"].count().reset_index()
    
    #revenue
    #st.write(f"Revenue of {choiceb}:")
    revenueb = new_datab["price"].sum()
    st.write(f"➙ Revenue of {choiceb}: **:red[$ {(revenueb)}]**")    
    #st.write(revenueb)
    sumperweekkb = new_datab.groupby(["week"])["price"].sum()
    
    #st.write(sumperweek)
    sumperweekkb = new_datab.groupby(["week"])["price"].sum().reset_index()
  
    #Calculate market share for SalesB
    salesB_revenue = datab['price'].sum()
    salesB_market_share = revenueb / salesB_revenue * 100
    st.write(f"➙ Market Share of {choiceb}: **:red[{salesB_market_share:.2f}%]**")
    #st.write(f"Market Share: {salesB_market_share:.2f}%")
    
    tab1b, tab2b = st.tabs(["Volume", "Revenue"])
    
    with tab1b:
      figvolb = px.line(sumperweekb, x="week", y="price", title='Volume through time')
      st.plotly_chart(figvolb)
    
    with tab2b:
      figrevb = px.line(sumperweekkb, x="week", y="price", title='Revenue through time')
      st.plotly_chart(figrevb)
      
    salesB_volum = datab.groupby(["company"])["price"].count()
    salesB_reve = datab.groupby(["company"])["price"].sum()
    salesB_market_share = datab.groupby(["company"])["price"].sum() / salesB_revenue * 100
  
    col1b, col2b, col3b = st.columns(3)

    with col1b:        
        st.write("Volume for each company")
        st.write(salesB_volum)
      
    with col2b:
        st.write("Revenue for each company")
        st.write(salesB_reve)
      
    with col3b:
        st.write("Market Share for each company")    
        st.write(salesB_market_share)
      
st.markdown('#')
st.markdown("<h1 style='font-family: Gill Sans Semibold, sans-serif; text-align: center;  font-weight: 600px, color: #C26F4D;'>Thank you 😄 </h1>", unsafe_allow_html=True)