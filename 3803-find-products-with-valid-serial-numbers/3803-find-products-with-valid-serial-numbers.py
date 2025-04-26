import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    pattern = r'\bSN\d{4}-\d{4}\b'
    products = products[products['description'].str.contains(pattern, regex=True)].sort_values(by='product_name')
    return products
    