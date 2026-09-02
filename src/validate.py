import pandas as pd
from src.extract import read_report
import numpy as np



# VALID — safe to use.
# FLAGGED — data exists, but needs investigation.
# INVALID — essential data is missing or unusable.

# rules 

    # Report_id - Required, Positive, unique
    # area - Required , not null, match known Areas
    # utilitty_type, Required, Electricity and water only
    # status - Required, outage or restored
    # reported at - valid_date and time , not be in future
    # source, Not required

def report_id_validator(row: pd.Series ) -> bool:

    '''
        Validate the report id only
    '''

    report_id = row.report_id
    if pd.isna(report_id):
        return False

    if isinstance(report_id, float):
        return False
    try:
        report_id = int(report_id)
        if report_id < 0:
            raise ValueError
    except ValueError:
        return False
    return True

def area_validator_check1(row: pd.Series) -> bool:
    '''
        Validate Area to check Null, Empty and return False
    '''
    if pd.isna(row.area) or len(str(row.area).strip()) == 0:
        return False
    return True


def area_validator_check2(row: pd.Series) -> str:
    '''
        Validate Area to check if the City Exists
    '''

    cites =[]
    area  = row.area
    try:
        int(area)
        return "Area is a Number"
    except ValueError:


        
        








def validate(df : pd.DataFrame) -> None:
    pass





if __name__ == "__main__":
    # file_name = "data/raw/outage_reports.csv"
    # df = read_report(file_name)
    # validate(df)
    df = pd.DataFrame({
    'report_id': ["sdsdsdsd", 'Bob'],
    'area': ["21", 30],
    'City': ['New York', 'Paris']
    })
    print(area_validator_check1(df.iloc[0]))