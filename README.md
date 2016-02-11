# Compare Datasets

So you got two datasets and you want to know if they are the same or different. If different then you would love an idea of how they are different. Well 'Compare Datasets' can help.

Enter 'Compare Datasets'. Compare datasets is python library that allows a quick, simple comparison of datasets. For simplicity let's say A is the 'original dataset' and B is the 'new dataset'

1. _Exact duplication_. The data, field names and order are the same. A = B.
1. _Additions_. B = A + some records and/or fields
1. _Subtractions_. B = A - some records and/or fields
1. _Updates_. B = Same identified rows as A, but with different values for those rows. Note: this check requires identifying the row ids.
1. _Same data, different fieldnames_. Sometimes the data isn't changed, but field names are tidied up. E.g. "First Name" vs First_Name. TODO(daniel) Determine how columns are matched between A and B. Do we compare common transformations on names, e.g. space to underscore, or do we compare blocks of the data and surmise its the 'same' field?
1. _Record Order_. Checks if A and B have records in the same order. Note: by default ignore_record_order = True. Set it to false if you care about order.
1. _Column Order_. Checks if A and B have fields in the same order. Note: by default ignore_field_order = True. Set it to false if you care about order.

The product of compare datasets is itself a dataset. This allows you to programmatic analysis. The fields of the output are 'Record Number', 'Check Name', 'Data Element in A', 'Data Element in B'

## Options
1. _Ignore Order_. Default False. When True, then row
1. _Ignore Column Order_.
1. _Igonre Row Order_.
1. _Ignore Whitespace_. Handy when comparing datasets with text.
1. _Specifiy Row Identifier_. Identify do not necessarily mean primary key. A row identifier may be repeated in a dataset. Required for the '_Updates_' check.



## FAQ
* Can I compare more than two datasets at once?  
 No. You would need to call Compare Datasets multiple times.
* Can I control the format of the output?  
 No. Unlike text (e.g. output unix's diff) dataframes are easily manipulated. Any required formatting is easy to do outside of 'Compare Datasets'
 * Can I diff arbitrary collection objects e.g. dictionaries?
 No. Look at the [DataDiff](https://sourceforge.net/projects/datadiff/.)
 package. 

## For comparison
* [R compare package]( http://www.inside-r.org/packages/cran/rioja/docs/compare.datasets)
* [Unix diff function](http://man7.org/linux/man-pages/man1/diff.1.html)
