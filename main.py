from utils import (
    load_and_clean_data,
    get_total_sales,
    get_total_orders,
    get_avg_order_value,
    get_top_products,
    get_monthly_sales,
    get_city_sales,
    get_hourly_sales
)

df = load_and_clean_data('data/sales.csv')


print(f" Total Sales: ${get_total_sales(df):,.2f}")
print(f" Total Orders: {get_total_orders(df)}")
print(f" Average Order Value: ${get_avg_order_value(df):.2f}")

print("\nTop 5 Products by Quantity Ordered:")
print(get_top_products(df))

print("\nSales per Month:")
print(get_monthly_sales(df))

print("\nSales per City:")
print(get_city_sales(df))

print("\nSales per Hour:")
print(get_hourly_sales(df))