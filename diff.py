"""

"""

import pandas as pd




def compare_cols(differences, cols_df1, cols_df2):
    # Check superset, subset
    fields_lost = ', '.join(set(cols_df1) - set(cols_df2))
    print "fields lost", fields_lost
    pd.concat([differences, {
        'test':'Fields lost',
        'result':fields_lost}],
        ignore_index=True, inplace=True)
    fields_added = ', '.join(set(cols_df2) - set(cols_df1))
    pd.concat([differences, {
        'test':'Fields added',
        'result':fields_added}],
        ignore_index=True, inplace=True)
    # TODO(daniel): Capture when order changes
    return differences

differences = pd.DataFrame({'test':[], 'result':[]})

df1 = pd.DataFrame({'a':[1,2,3], 'b':[6,7,8]})
df2 = pd.DataFrame({'a':[1,2,3], 'c':[6,7,8]})

compare_cols(differences, df1.columns.values, df2.columns.values)

print differences
