# BIDashboard
An upgraded version of an old BIDashboard project
The aim of this project was to learn how BI works and what a dashboard is concretly

```
BIDashboard/
├── data/
│   └── sales.csv         # sales dataset
├── utils.py              # contains the functions to clean data and extract KPIs
├── main.py               # CLI display
└── app.py                # new Dashboard GUI using Streamlit
```

to run the program you will need Pandas library and Streamlit framework
```
pip3 install pandas
pip3 install streamlit
```
Then to run it
```
streamlit run app.py
``` 

The old version had only a CLI display of the KPIs and had filtered results.
This version incorporates a framework for data visualisation (Streamlit) to give better view of KPIs.

The dataset used is a classic sales public dataset found in Kaggle containing Sales of products for 12 months period.
The dataset consists of 11 columns, each column representing an attribute of purchase on a product -
- <b>Order</b> ID - A unique ID for each order placed on a product
- <b>Product</b> - Item that is purchased
- <b>Quantity Ordered</b> - Describes how many of that products are ordered
- <b>Price Each</b> - Price of a unit of that product
- <b>Order Date</b> - Date on which the order is placed
- <b>Purchase Address</b> - Address to where the order is shipped

The KPIs calculated and displayed are: 
- Total Sales 
- Total Orders
- Sales per Hour
- Most Profitable Product

All the results can be filtered by:
- Month
- City

