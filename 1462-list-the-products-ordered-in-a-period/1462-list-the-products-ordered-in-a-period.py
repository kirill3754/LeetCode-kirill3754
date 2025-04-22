import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.query("'2020-02-01'<=order_date<'2020-03-01'")
    orders = orders.groupby('product_id', as_index=False)['unit'].sum()
    orders = orders.query("unit>=100")
    orders = orders.merge(products[['product_id', 'product_name']], on='product_id', how='left')
    orders = orders.drop(columns='product_id')
    return orders[['product_name', 'unit']]
    