import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = pd.merge(orders, sales_person, how='left', on='sales_id')
    orders = pd.merge(orders, company, how='left', on='com_id', suffixes=(None, '_comp'))
    orders = orders[orders['name_comp'] == 'RED']
    orders = orders[['name', 'name_comp']]
    sales_person = pd.merge(sales_person, orders, how='left', on='name')
    sales_person = sales_person[sales_person['name_comp'] != 'RED'][['name']]
    return sales_person
    