import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    pivot_df = department.pivot(index='id', columns='month', values='revenue').reindex(columns=columns).reset_index()
    pivot_df.columns = ['id'] + [f'{column}_Revenue' for column in columns]
    return pivot_df
    