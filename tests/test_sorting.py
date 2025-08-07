from algorithms.sorting import quicksort

def test_quicksort():
    assert quicksort([3,1,2]) == [1,2,3]
    assert quicksort([]) == []
    assert quicksort([5]) == [5]
