import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person = person[person.duplicated(subset = ['email'], keep=False)][['email']].drop_duplicates()
    return person

    