
import random
import uuid


def generate_order_parts_data(order_id: str, auto_parts: list[dict], num_parts: int) -> list[dict]:
    """
        SCHEMA:
            id          String(UUID)
            order_id    String(UUID) [Foreign Key -> Orders table]
            part_id     String(UUID) [Foreign Key -> AutoPart table]
            quantity    Integer
            unit_price  Float
            total_price Float
    """

    # Select randomly "num_parts" elements from auto_parts list.
    random_auto_parts = random.sample(auto_parts, num_parts)

    # Generate order_products data.
    order_auto_parts, total_amount = [], 0
    for product in random_auto_parts:
        quantity = random.randint(1, 4)
        total_amount += quantity * product.get("price")

        order_auto_parts.append({
            "id": str(uuid.uuid4()),
            "order_id": order_id,
            "product_id": product.get("id"),
            "unit_price": product.get("price"),
            "quantity": quantity,
            "total_price": product.get("price") * quantity
        })

    return round(total_amount, 2), order_auto_parts