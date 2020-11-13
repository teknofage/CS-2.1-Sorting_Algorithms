#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
        Running time: 
            O(n) * m  
        Why and under what conditions? 
            Because it needs to read both arrays until it reaches the end of one of them.
            This is also when extra space is not allowed.
        Memory usage: 
            O(1) or O(n)
        Why and under what conditions?
            Not creating new structures beyond the merging of the two lists
        """
    # if both items1 and items2 exist
    if items1 and items2:
    # Find lowest first value between two lists
        if items1[0] > items2[0]:
            # if lowest value in second list, swap lists
            items1, items2 = items2, items1
        # Find minimum item in both lists and append it to new list
        # Repeat until one list is empty
        # Append remaining items in non-empty list to new list
        return [items1[0]] + merge(items1[1:], items2)
    return items1 + items2
# print(merge([5,6,7],[1,2,3]))


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
        Running time: 
            (n log(n))
        Why and under what conditions?
            Under average conditions
        Memory usage: 
            O(n)
        Why and under what conditions?
            Creating no new data structures. 
        """
    # Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    # Split items list into approximately equal halves
    middle = len(items) // 2
    # make left section equal to items from start to middle
    left = items[:middle]
    # make right section equal to items from middle to end
    right = items[middle:]
    # Sort each half by recursively calling merge sort    
    merge_sort(left)
    merge_sort(right)

    # declare 3 variable all equal to 0
    i = j = k = 0
    # don't go over the length of lists
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            # set first variable[k] in items  equal to index [i] of left
            items[k] = left[i]
            # iterate i
            i += 1
        else:
            items[k] = right[j]
            # iterate j
            j += 1
        # iterate k
        k += 1
    # as long as index i is less than the length of the left sub-array
    while i < len(left):
        # set items[k] index as equal to left[i] index
        items[k] = left[i]
        # iterate i and k
        i += 1
        k+= 1
    # as long as index j is less than the length of the right sub-array
    while j < len(right):
        # set items[k] index as equal to right[j] index
        items[k] = right[j]
        # iterate j and k
        j += 1
        k += 1
        # Merge sorted halves into one list in sorted order
    return items
        
print(merge_sort([6,8,7,1]))


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot from the end of the array, 
    and at the end of the higher partition, 
    moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
        Running time: 
            log(n) 
        Why and under what conditions?
            Only splitting array
        Memory usage: 
            ??? 
        Why and under what conditions?
        
        """
    # create variable i and set it equal to the index to the left of the low partition
    i = low - 1
    # Choose a pivot any way and document your method in docstring above
    pivot = items[high]
    # Loop through all items in range [low...high]
    for j in range(low, high):
        if items[j] < pivot:
            i += 1
            # Move items less than pivot into front of range [low...p-1]
            # Move items greater than pivot into back of range [p+1...high]
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[high] = items[high], items[i + 1]
    # Move pivot item into final position [p] and return index p
    return (i + 1)
            

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
        Best case running time: 
            O(n log(n))
        Why and under what conditions?
            Multiple passes are required, and the a short array means less passes, 
            and less sorting. 
            Also, choosing the appropriate pivot that splits the array evenly 
            can speed things up a lot.
        Average case running time: 
            O(n log(n))
        Why and under what conditions?
            Each element gets quicksort called on it (log n) times.
            n elements go through (log n) swaps
        Worst case running time: 
            O(n^2)
        Why and under what conditions?
            Longer array means more passes and more sorting, meaning more time. 
            Also, choosing a less suitable pivot that does not split the array evenly 
            can slow it down a lot, such as the smallest or largest element.
        Memory usage: 
            Worst: O(log(n))
        Why and under what conditions?
            Uses minimal extra memory by not creating extra data structures. 
        """
    # Check if list or range is so small it's already sorted (base case)
    if low >= high:
        # list is sorted
        return
    else:
        pivot = partition(items, low, high)
        # Check if high and low range bounds have default values (not given)
 
        
        
    # Partition items in-place around a pivot and get index of pivot
    # Sort each sublist range by recursively calling quick sort
 
    
    


def quick_sort(items, low=None, high=None):
    length = len(items)
    # Check if list or range is so small it's already sorted (base case)
    if length <= 1:
        # return list: it is already sorted
        return items
    else:
        # create pivot by using the last item in the array and removing it from the array
        pivot = items.pop()

    # items lower than the pivot
    low = []
    # items higher than the pivot
    high = []
    
    # iterate through items
    for item in items:
        # if the item is greater than the pivot
        if item > pivot:
            # append it to the array of items higher than the pivot
            high.append(item)
        else:
            # or else append it to the array of items lower than the pivot
            low.append(item)
    # call quick_sort recursively on the lower half, and the higher half, and 
    # put the pivot in the middle, and return the result
    return quick_sort(low) + [pivot] + quick_sort(high)

items = [2,3,6,3,7,5,8,9,7,6]    
print(quick_sort(items, 0, 9))