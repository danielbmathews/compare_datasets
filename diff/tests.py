import unittest
import pandas as pd
import diff

class CompareColumnsTest(unittest.TestCase):

    ''' Test for compare_column_names'''

    def test_compare_column_names(self):
        df1 = pd.DataFrame({'a':[1, 2, 3], 'b':[2, 2, 2]})
        df2 = pd.DataFrame({'a':[1, 2, 3], 'b':[2, 2, 2]})
        df3 = pd.DataFrame({'a':[1, 2, 3], 'c':[2, 2, 2]})

        # comapare df1 and df2 columsn - which are identical
        self.assertEqual(diff.compare_column_names(df1, df2)['added column(s)'], [])
        self.assertEqual(diff.compare_column_names(df2, df1)['added column(s)'], [])
        self.assertEqual(diff.compare_column_names(df2, df1)['missing column(s)'], [])

        # compare df1 and df3 columsn - which are different
        self.assertEqual(diff.compare_column_names(df1, df3)['added column(s)'], ['c'])
        self.assertEqual(diff.compare_column_names(df1, df3)['missing column(s)'], ['b'])
