import random
import uuid

from faker import Faker
from datetime import date

faker = Faker()


def generate_order_data(rows_num: int, users_data: dict) -> str:
    """
        SCHEMA:
            id              String(UUID)
            user_id         String(UUID) [Foreign Key -> Users Table]
            order_date      DateTime
            status          Status
            total_amount    Float
            payment_method  PaymentMethods
            is_paid         Boolean
    """

    status: list = ["Placed", "Processing", "In delivery", "Delivered", "Cancelled"]
    payment_methods: list = ["Card", "Card on Delivery", "Cash on Delivery"]
    orders = list()

    for _ in range(rows_num):
        order_status = random.choice(status)
        payment_method = random.choice(payment_methods)
        is_paid = True if (order_status in ["Delivered"]) or (order_status in ["Processing", "In delivery"] and payment_method == "Card") else False
        user = random.choice(users_data)
        
        orders.append({
            "id": str(uuid.uuid4()),
            "user_id": user.get("id"),
            "order_date": faker.date_between(start_date=user.get("registered_on"), end_date="today"),
            "status": order_status,
            "total_amount": 0,
            "payment_method": payment_method,
            "is_paid": is_paid
        })

    return orders


