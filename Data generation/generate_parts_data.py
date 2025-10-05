import random
import uuid
import pandas as pd


def get_root(id_parent_id_mapping: dict[str, str], id_name_mapping: dict[str, str], category_id: str) -> dict[str, str]:
    """
        Traverse the parent hierarchy to find the root category for a given category_id.

        Returns:
            dict: {"Category": root_category_name, "Part Name": leaf_category_name}
    """
    
    parent = id_parent_id_mapping.get(category_id)

    while id_name_mapping.get(id_parent_id_mapping.get(parent)):
        parent = id_parent_id_mapping.get(parent)
    
    return {
        "Category": id_name_mapping.get(parent), 
        "Part Name": id_name_mapping.get(category_id)
    }


def generate_autopart_data(rows_num: int, products_file_path: str) -> list[dict]:
    """
        SCHEMA:
            id           String(UUID)  
            name         String
            category     Category
            price        Double
            stock        Integer
            brand        Brand
            weight       Double
    """

    # Read data from the CSV file.
    df_product = pd.read_csv(products_file_path, dtype=str).dropna()

    # Create a brands list.
    brands: list = ["Valeo", "Bosch", "MANN-FILTER", "Denso", "Magna", "ZF", "Continental", "Autoliv"]

    # Determine leaf categories (they will represent the general part names).
    leaf_categories = set(df_product['id']) - set(df_product['parent_category_id'])

    # Create two mapping dictionaries; one for mapping between {id, parent} and one for mapping {id, category_name}.
    id_parent_id_mapping: dict = dict(zip(df_product["id"], df_product["parent_category_id"]))
    id_name_mapping: dict = dict(zip(df_product["id"], df_product["category_name"]))

    # Create the category -> parts list.
    category_parts: list = [get_root(id_parent_id_mapping, id_name_mapping, leaf) for leaf in leaf_categories]

    # Generate auto part data.
    parts: list = []
    for _ in range(rows_num):
        category_part: dict = random.choice(category_parts)

        # Create and add the auto part to the list.
        parts.append({
            "id": str(uuid.uuid4()),
            "name": category_part.get("Part Name"),
            "category": category_part.get("Category"),
            "price": round(random.uniform(5, 500), 2),
            "stock": random.randint(0, 100),
            "brand": random.choice(brands),
            "weight": round(random.uniform(0.4, 15), 2)
        })

    return parts