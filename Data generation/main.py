import random
import pandas as pd

from generate_users import generate_user_data
from generate_parts_data import generate_autopart_data
from generate_order_data import generate_order_data
from generate_orders_parts_data import generate_order_parts_data


# Generate 1000 users and save the data to a CSV file.
users = generate_user_data(1000)
df_users = pd.DataFrame(users)
df_users.to_csv(r"Data generation/users.csv", index=False)

# Generate 1000 auto parts and save the data to a CSV file.
parts = generate_autopart_data(1000, r"Data generation/product_category.csv")
df_parts = pd.DataFrame(parts)
df_parts.to_csv(r"Data generation/autoparts.csv", index=False)

# Generate 1000 orders and save the data to a CSV file.
# Initially the "total_amount" field will be empty for every order. It will be calculated after the "orders_products" table will be generated.
orders = generate_order_data(1000, users)

# For every order, generate a random number of auto parts. Then, generate random details about them.
# Calculate the total amount based on the total_price of every product.
orders_parts = []
for order in orders:
    total_amount, order_parts = generate_order_parts_data(order.get("id"), parts, random.randint(1, 4))
    order["total_amount"] = total_amount
    orders_parts.extend(order_parts)

# Write order data to CSV files.
df_orders = pd.DataFrame(orders)
df_orders.to_csv(r"Data generation/orders.csv", index=False)

# Write Orders Data to CSV.
df_orders_parts = pd.DataFrame(orders_parts)
df_orders_parts.to_csv(r"Data generation/orders_parts.csv", index=False)