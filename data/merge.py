import pandas as pd

# Load datasets
order_payments = pd.read_csv('order_payments_dataset.csv')
customers = pd.read_csv('customers_dataset.csv')
order_items = pd.read_csv('order_items_dataset.csv')
order_reviews = pd.read_csv('order_reviews_dataset.csv')
orders = pd.read_csv('orders_dataset.csv')
product_category_translation = pd.read_csv('product_category_name_translation.csv')
products = pd.read_csv('products_dataset.csv')
sellers = pd.read_csv('sellers_dataset.csv')

# Merge orders with customers on customer_id
orders_customers = pd.merge(orders, customers, on='customer_id', how='left')

# Merge order_items with products on product_id
order_items_products = pd.merge(order_items, products, on='product_id', how='left')

# Merge order_items with orders on order_id
order_items_orders = pd.merge(order_items_products, orders, on='order_id', how='left')

# Merge order_payments with orders on order_id
order_payments_orders = pd.merge(order_payments, orders, on='order_id', how='left')

# Merge order_reviews with orders on order_id
order_reviews_orders = pd.merge(order_reviews, orders, on='order_id', how='left')

# Optional: Merge product categories with translated names
products_translated = pd.merge(products, product_category_translation, on='product_category_name', how='left')

# Save merged datasets to new CSV files
orders_customers.to_csv('merged_orders_customers.csv', index=False)
order_items_products.to_csv('merged_order_items_products.csv', index=False)
order_items_orders.to_csv('merged_order_items_orders.csv', index=False)
order_payments_orders.to_csv('merged_order_payments_orders.csv', index=False)
order_reviews_orders.to_csv('merged_order_reviews_orders.csv', index=False)
products_translated.to_csv('translated_products.csv', index=False)

print("Merged data saved to CSV files.")
