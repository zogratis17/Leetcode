import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df_cus=customers[~customers['id'].isin(orders['customerId'])]      
    return df_cus[['name']].rename(columns={'name':'Customers'})