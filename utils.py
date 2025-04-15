import pandas as pd


def load_and_clean_data(fp):
    df = pd.read_csv(fp)
    
    # clean the data
    df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'], errors='coerce')
    df['Price Each'] = pd.to_numeric(df['Price Each'], errors='coerce')
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df.dropna(inplace=True)
    
    df['Sales'] = df['Quantity Ordered'] * df['Price Each']
    df['Month'] = df['Order Date'].dt.month
    df['Hour'] = df['Order Date'].dt.hour
    df['City'] = df['Purchase Address'].apply(lambda x: f"{x.split(',')[1].strip()} ({x.split(',')[2].strip().split(' ')[0]})")
    
    return df

def get_total_sales(df):
    return df['Sales'].sum()

def get_total_orders(df):
    return df['Order ID'].nunique()

def get_avg_order_value(df):
    return get_total_sales(df) / get_total_orders(df)

def get_top_products(df, n=5):
    return df.groupby('Product')['Quantity Ordered'].sum().sort_values(ascending=False).head(n)

def get_monthly_sales(df):
    return df.groupby('Month')['Sales'].sum()

def get_city_sales(df):
    return df.groupby('City')['Sales'].sum().sort_values(ascending=False)

def get_hourly_sales(df):
    return df.groupby('Hour')['Sales'].sum().sort_values(ascending=False)

def get_most_profitable_product(df):
    return df.groupby('Product')['Sales'].sum().idxmax()

