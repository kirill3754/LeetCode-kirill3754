import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r"^[a-zA-Z][\w\.-]*@leetcode\.com$"
    users = users[users['mail'].str.match(pattern)]
    return users