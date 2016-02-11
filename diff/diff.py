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

# TODO(daniel) General compare_* function. Comparing column names or rows or
# anything is fundamentally the same operation. Comparing column names is a
# standard call. Comparing dataframes rows take two iterations i.e. one to
# find which rows are different, second to identify individual values that
# are different.

def compare_lists(A, B):
    results = dict()
    # Check for equality, with order & ignoring order
    if A == B:
        results['equality check with order'] = True
    elif set(A) == set(B):
        results['equality check without order'] = True
    else:
        results['elements'] = 'Different'
    # check for added elements
    added = list(set(A) - set(B))
    if added:
        results['added elements'] = added
    # check for lost elements
    lost = list(set(B) - set(A))
    if lost:
        results['lost elements'] = lost
    return results

def diff_lists(list_1, list_2):
    results = dict()
    # Check for equality, with order & ignoring order
    if list_1 == list_2:
        results['equality check with order'] = True
    elif set(list_1) == set(list_2):
        results['equality check without order'] = True
    else:
        results['elements'] = 'Different'
    # check for added elements
    added = list(set(list_1) - set(list_2))
    if added:
        results['added elements'] = added
    # check for lost elements
    lost = list(set(list_2) - set(list_1))
    if lost:
        results['lost elements'] = lost
    return results
