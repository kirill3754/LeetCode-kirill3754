import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    n_users = len(users)
    df = register['contest_id'].value_counts().reset_index()
    df.columns = ['contest_id','percentage']
    df['percentage'] = round(df['percentage']*100/n_users,2)
    df = df.sort_values(by=['percentage', 'contest_id'], ascending=[False, True]).reset_index(drop=True)
    return df