from timeit import timeit
import numpy as np
import builtins
from IPython import get_ipython

def completely_sorted_list(N):
    """
    Create a list of size N that is already sorted.
    """
    return list(range(N))

def reversed_list(N):
    """
    Create a list of size N, sorted in reversed order.
    """
    # or e.g. list(range(N-1,-1,-1))
    return completely_sorted_list(N)[::-1]

def nearly_sorted_list(N):
    """
    Create a list of size N, sorted but for approximately 10% of elements out of place.
    We will move k elements, where k = N//10.
    The k elements are chosen one at a time, so we do not guarantee exactly k elements
    out of place.
    """
    k = N//10
    # Move at least one element
    if N>0 and k<1:
        k = 1
    l = completely_sorted_list(N)
    for i in range(k):
        index_to_move = np.random.randint(N)
        value = l[index_to_move]
        # remove the element
        l = l[0:index_to_move] + l[index_to_move+1:]
        # slot it back in
        new_position = np.random.randint(N-1)
        l = l[0:new_position] + [value] + l[new_position:]
    return l

def random_list(N):
    """
    Create a list of size N, shuffled randomly.
    """
    items = completely_sorted_list(N)
    np.random.shuffle(items)
    return items

def time_sort(sort_function, input_list):
    """
    Time a sort function on a given input list using timeit.
    Makes use of a global variable unsorted_list, which will be overwritten.
    Assumes we are being called from an IPython/Jupyter context and adds the
    IPython namespace to the local namespace.
    """
    num_runs = 1000
    return timeit("sort_function(input_list)", number=num_runs)/num_runs

