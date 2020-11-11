#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
        Running time: 
            O(n) * m  
        Why and under what conditions? 
            Because it needs to read both arrays until it reaches the end of one of them.
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    # TODO: Split items list into approximately equal halves
    middle = len(items) // 2
    left = items[0:middle + 1]
    right = items[middle + 1]
    
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def choose_pivot(items):
    # make pivot equal to first item in array
    pivot = items[0]
    return pivot

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
        Best case running time: 
            O(n log(n))
        Why and under what conditions?
            Multiple passes are required, and the a short array means less passes and less sorting. 
            Also, choosing the appropriate pivot can speed things up a lot.
        Average case running time: 
            O(n log(n))
        Why and under what conditions?
            Each element gets quicksort called on it (log n) times.
            n elements go through (log n) swaps
        Worst case running time: 
            O(n^2)
        Why and under what conditions?
            Longer array means more passes and more sorting, meaning more time. 
            Also, choosing a less suitable pivot can slow it down a lot.
        Memory usage: 
            Worst: O(log(n))
        # TODO: Why and under what conditions?
            Uses minimal extra memory by not creating extra data structures. 
        """
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    
    
items = [2,3,6,3,7,5,8,9,7,6]    
quick_sort(items, 0, 9)