import pandas as pd


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


def read_report(csv_file) -> pd.DataFrame:
    '''
        This func just returns a dataFrame, Reads a location fileName
    '''
    return pd.read_csv(csv_file)
