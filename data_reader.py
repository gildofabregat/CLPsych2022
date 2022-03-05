"""Read txt/csv file as input."""
import pandas as pd
import numpy as np


def csv_reader(path: str) -> pd.DataFrame:
    """Read & process TSV file.
    
    Parameters
    ----------
    path: str
        path to TSV file.

    Returns
    -------
    df: pd.DataFrame
        dataframe containing timelines of a user.
    """
    df = pd.read_csv(path, sep='\t')
    df = process_data(df)

    return df

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """Process input dataframe.

    Parameters
    ----------    
    df: pd.DataFrame
        Raw dataframe containing timelines.

    Returns
    -------
    df: pd.DataFrame
        processed dataframe
    """
    # Processing commands
    # --------------

    # ---------------
    return df