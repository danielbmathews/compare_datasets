''' diff This module contains the core diff function for comparing pandas
dataframes. This class takes two dataframes (df1, df2) and generates a
difference dataframe. df1 is assumed to be the base dataframe and df2 is
compared to it. The difference dataframe has #1 tests, #2 results, #3 as needed
specific details of the results. '''

import pandas as pd
from collections import namedtuple

testresults = namedtuple('TestResult', ['test', 'results'])


class TestResult:
    'An object to collect and display the results of tests'

    def __init__(self):
        'Create list to hold test names and results.'
        self.results = []

    def add_result(self, test, results):
        self.results.append(testresults(test, results))

    def display_results(self):
        for i, item in enumerate(self.results):
            print 'Test #', i
            print self.results[i].test
            print self.results[i].results
            print '\n'

x = TestResult()
x.add_result("test1", "result1")
x.add_result("test2", "result2")

x.display_results()


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

def diff_dfs():
    pass



# TODO(daniel) Comparing dataframes rows take two iterations i.e. one to
# find which rows are different, second to identify individual values that
# are different.
