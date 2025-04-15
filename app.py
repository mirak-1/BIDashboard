import streamlit as st
import pandas as pd
from utils import (
    load_and_clean_data,
    get_total_sales,
    get_total_orders,
    get_avg_order_value,
    get_top_products,
    get_monthly_sales,
    get_city_sales,
    get_hourly_sales,
    get_most_profitable_product
)

from filters import filter_by_month, filter_by_city

df = load_and_clean_data("data/sales.csv")

st.sidebar.title("Filters")
months = sorted(df['Month'].unique())
months_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
selected_month = st.sidebar.selectbox("Select Month", ["All"] + [str(m) +" - " + name for m, name in zip(months, months_names)]).split(" - ")[0]
filtered_df_month = filter_by_month(df, selected_month)
    
cities = sorted(df['City'].unique())
selected_city = st.sidebar.selectbox("Select City", ["All"] + [str(m) for m in cities])
filtered_df_city = filter_by_city(filtered_df_month, selected_city)

filtered_df = filtered_df_city
st.title("Sales Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${get_total_sales(filtered_df):,.2f}")
col2.metric("Total Orders", get_total_orders(filtered_df))
col3.metric("Avg Order Value", f"${get_avg_order_value(filtered_df):.2f}")

col = st.columns(1)
col1.metric("Most Sold Product", f"${get_most_profitable_product(filtered_df)}")

# top products
st.subheader("Top Selling Products")
st.dataframe(get_top_products(filtered_df))

# by city
st.subheader("Sales by City")
st.bar_chart(get_city_sales(filtered_df))

# sales by hour
st.subheader("Sales by Hour")
st.line_chart(get_hourly_sales(filtered_df))