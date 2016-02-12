from diff import diff_lists

list_1 = [1, 2, 3]
list_2 = [2, 1, 4, 5, 6]

def test_diff_lists():
    assert diff_lists(list_1, list_1)['added elements'] == []
    assert diff_lists(list_1, list_1)['lost elements'] == []

    # compare df1 and df3 columsn - which are different
    assert diff_lists(list_1, list_2)['added elements'] == [4, 5, 6]
    assert diff_lists(list_1, list_2)['lost elements'] == [3]
