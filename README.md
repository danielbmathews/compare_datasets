# Compare Datasets

So you got two datasets and you want to know if they are the same or different. If different then you would love an idea of how they are different. Well 'Compare Datasets' can help.

Enter 'Compare Datasets'. Compare datasets is python library that allows a quick, simple comparison of datasets. For simplicity let's say A is the 'original dataset' and B is the 'new dataset'

1. _Exact duplication_. A = B.
1. _Additions_. B = A + some records and/or fields
1. _Subtractions_. B = A - some records and/or fields
1. _Updates_. B = Same identified rows as A, but with different values for those rows.
1. _Record Order_. Checks if A and B have records in the same order. Note: by default ignore_record_order = True. Set it to false if you care about order.
1. _Column Order_. Checks if A and B have fields in the same order. Note: by default ignore_field_order = True. Set it to false if you care about order.


Optional denote row identifier. Identify do not necessarily mean primary key. A row identifier may be repeated in a dataset.

## FAQ
* Can I compare more than two datasets at once?
No. You would need to call Compare Datasets multiple times.
* What do you mean by optional row identifier?

## For comparison
R [compare package]( http://www.inside-r.org/packages/cran/rioja/docs/compare.datasets)
