import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    customers = customers[customers['id_y'].isna()]
    customers = customers[['name']]
    customers.rename(columns={'name': 'Customers'}, inplace = True)
    return customers

    