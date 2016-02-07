''' diff This module contains the core diff function for comparing pandas
dataframes. This class takes two dataframes (df1, df2) and generates a
difference dataframe. df1 is assumed to be the base dataframe and df2 is
compared to it. The difference dataframe has #1 tests, #2 results, #3 as needed
specific details of the results. '''

import pandas as pd


class TestResults(object):
    """An object to collect and display the results of tests"""

    def __init__(self):
        pass

    def add_result(self, result):
        pass

    def display_results(self):
        pass

def compare_column_names(df1, df2):
    results = dict()
    df1_cols = df1.columns.tolist()
    df2_cols = df2.columns.tolist()
    # Are the columns identical
    if df1_cols == df2_cols:
        results['column names'] = 'same, including order'
    elif set(df1_cols) == set(df2_cols):
        results['column names'] = 'same, but different order'
    else:
        results['column names'] = 'different'

    # Does df2 have additional columns?
    df2_added_columns = list(set(df2_cols) - set(df1_cols))
    results['added column(s)'] = df2_added_columns

    # Does df2 have missing columns?
    df2_missing_columns = list(set(df1_cols) - set(df2_cols))
    results['missing column(s)'] = df2_missing_columns
    return results

def compare_columns(df1, df2):
    results = dict()
    pass
