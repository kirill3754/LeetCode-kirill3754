import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    person = pd.merge(person, address, on='personId', how='left')
    person = person.get(["firstName", "lastName", "city", "state"])
    return person

    