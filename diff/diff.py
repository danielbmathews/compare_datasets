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


def diff_lists(A, B):
    results = dict()
    # Check for equality, with order & ignoring order
    if A == B:
        results['equality check with order'] = True
    elif set(A) == set(B):
        results['equality check without order'] = True
    else:
        results['elements'] = 'Different'
    # Check for added and lost elements
    results['added elements'] = [b for b in B if b not in A]
    results['lost elements'] =  [a for a in A if a not in B]

    return results

# TODO(daniel) General compare_* function. Comparing column names or rows or
# anything is fundamentally the same operation. Comparing column names is a
# standard call. Comparing dataframes rows take two iterations i.e. one to
# find which rows are different, second to identify individual values that
# are different.
