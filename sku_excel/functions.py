import sqlite3
def get_height_from_sku(sku: str):
    return int("".join(letter for letter in sku if letter.isdigit()))

def add_product_versions_to_db(db_file, table_versions, versions):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    for version in versions:
        cursor.execute(
            f"INSERT INTO {table_versions} (product_id, name, sku) VALUES (?, ?, ?)",
            version
        )

    conn.commit()
    conn.close()


def get_products_from_db(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    # noinspection SqlNoDataSourceInspection
    products = cursor.execute("SELECT * FROM production_product").fetchall()
    conn.commit()
    conn.close()
    return products

def generate_product_versions_sku(products, dimensions):
    versions = []
    for product in products:
        versions.extend(
            (
                product[0],
                f"{dimension[0]}x{dimension[1]}-{' '.join(product[1].split()[:4])}",
                f"{product[3][:-4]}-{dimension[0]}x{dimension[1]}",
            )
            for dimension in dimensions
        )
    return versions