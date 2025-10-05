import uuid
import random

from faker import Faker
from datetime import date

faker = Faker()


def generate_user_data(rows_num: int) -> list[dict]:
    """
        SCHEMA: 
            id             String(UUID)   
            first_name     String
            last_name      String
            email          String  
            phone_number   String
            password       String
            registered_on  DateTime
            is_verified    Boolean  
            is_subscribed  Boolean 
            role           Role
    """

    roles = ["Client", "Operator", "Admin"]
    users = []

    for _ in range(rows_num):
        # Generate the first and last names.
        first_name: str = faker.first_name()
        last_name: str = faker.last_name()

        # Based on the generated first and last name, create an email address.
        email: str = first_name.lower() + last_name.lower() + "@" + random.choice(["gmail", "yahoo"]) + ".com"

        # Generate random values for the verified and subscribed fields. Only verified users can subscribe to notifications.
        is_verified: bool = random.choice([False, True])
        is_subscribed: bool = False if not is_verified else random.choice([False, True])

        # Create and add the user to the list.
        users.append({
            "id": str(uuid.uuid4()),
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": faker.phone_number(),
            "password": faker.password(),
            "registered_on": faker.date_between(start_date=date(2024, 7, 1), end_date="today"),
            "is_verified": is_verified,
            "is_subscribed": is_subscribed,
            "role": random.choice(roles)
        })

    return users