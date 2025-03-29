import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee = pd.merge(employee, employee, left_on = 'managerId', right_on = 'id')
    filtered = employee[employee['salary_x'] > employee['salary_y']][['name_x']]
    ans = filtered.rename(columns={'name_x': 'Employee'})
    return ans


    