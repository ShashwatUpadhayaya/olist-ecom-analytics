import streamlit as st
import pandas as pd
import sqlite3

#Setting the page config:
st.set_page_config(page_title= "E-com analytics", layout= "wide")
st.title("OLIST E-com analytics dashboard.")
st.markdown("Welcome to this interactive dashboard, bellow you will find the joined database")

#Connection to the local db I created in ingestion:
conn = sqlite3.connect("ecommerce_data.db")

#Lets see how many rows we have
total_orders_query = "SELECT COUNT(order_id) FROM orders_customers"
total_orders = pd.read_sql(total_orders_query, conn).iloc[0,0]
st.subheader("Key Performance Indicators")
#I'll use metric fxn to make a good KPI box:
st.metric(label = "Total Orders Processed", value = f"{total_orders:,}")
st.divider()

#Grouping the data and counting the orders which they fall into for their status:
status_query = """
SELECT order_status, COUNT(order_id) as count
FROM orders_customers
GROUP BY order_status
"""
status_df = pd.read_sql(status_query, conn)
st.subheader("Order status distribution")

#Now to set index to the status name for streamlit to draw "X":
st.bar_chart(status_df.set_index("order_status"))

#A problem of skewed data arises, so along with showing the sucess of our data, we will also show the rest of the value-orders for the company to see and evaluate:
st.subheader("Non-delivered orders distribution")
#To do this, we eliminate the highly sucessful delivered bar so the resto f the data is easier to analyse:
exception = status_df[status_df["order_status"] != "delivered"]
st.bar_chart(exception.set_index("order_status"))

st.divider()
st.subheader("Peak sales periods(Time series)")
st.markdown("Traking monthly order volumes to identify seasonal data patterns")

sales_query = """
SELECT strftime('%Y-%m',order_purchase_timestamp) AS order_month,
    COUNT(order_id) AS total_orders
FROM orders_customers
WHERE order_purchase_timestamp IS NOT NULL
GROUP BY order_month
ORDER BY order_month
"""
sales_trend_df = pd.read_sql(sales_query,conn)
st.line_chart(sales_trend_df.set_index("order_month"))

st.divider()
st.header("Delivery bottlenecks")
st.markdown("5 Staes with most delivery bottlenecks")
bottle_query = """
SELECT
    customer_state,
    COUNT(order_id) AS total_orders,
    SUM(CASE WHEN order_delivered_customer_date>order_estimated_delivery_date THEN 1 ELSE 0 END) AS late_orders,
    ROUND((SUM(CASE WHEN order_delivered_customer_date>order_estimated_delivery_date THEN 1 ELSE 0 END)*100.0/COUNT(order_id)),2) AS delay_percentage
FROM orders_customers
WHERE order_status = 'delivered'
    AND order_delivered_customer_date IS NOT NULL
    AND order_estimated_delivery_date IS NOT NULL
GROUP BY customer_state
HAVING total_orders>100
ORDER BY delay_percentage DESC
LIMIT 5        
"""
delay_df = pd.read_sql(bottle_query, conn)
st.bar_chart(delay_df.set_index("customer_state")["delay_percentage"])

conn.close()
