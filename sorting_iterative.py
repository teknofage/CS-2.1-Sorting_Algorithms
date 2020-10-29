#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(1)    
    Why and under what conditions? Not running through any loops and it uses a constant time.
    Memory usage: O(1)    
    Why and under what conditions? No new structures are created or changed so the memory usage is linear."""
    copy = items[:]
    copy.sort()
    return copy == items


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: Best: O(n), Average: O(n^2), Worst: O(n^2)       
    Why and under what conditions? Best: single iteration, but Worst would involve several passes of iteration.
    Memory usage: O(1)            
    Why and under what conditions? No new structures are created or changed so the memory usage is linear."""
    is_sorted = True
    counter = 0
    while(is_sorted):
        is_sorted = False
        for i in range(len(items) - counter - 1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                is_sorted = True
        counter += 1

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: Best: O(n), Average: O(n^2), Worst: O(n^2)       
    Why and under what conditions?  Best conditions mean looping through a small list of items, and worst conditions require looping through a large list of items, and therefore requiring more time the larger the list is.
    Memory usage: O(1)                 
    Why and under what conditions? No new structures are created or changed, resulting in little memory being used."""
        # i indicates how many items were sorted
    for i in range(len(items)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(items)-1):
            # Update the min_index if the element at j is lower than it
            if items[j] < items[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        items[i], items[min_index] = items[min_index], items[i]
"""Now let's add some code to the file to test the algorithm:"""

items = [3, 1, 41, 59, 26, 53, 59]
print(items)
selection_sort(items)

# Let's see the list after we run the Selection Sort
print(items)


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: Best: O(n), Average: O(n^2), Worst: O(n^2)      
    Why and under what conditions?  Best case only requires linear run time due to small list of items, and Worst case would use a large list of items.
    Memory usage: O(1)            
    Why and under what conditions? No new structures are created or changed so memory usage is minimal. """
    item_length = range(1, len(items))
    for i in item_length:
        unsorted_value = items[i]

        while items[i-1] > unsorted_value and i > 0:
            items[i], items[i-1] = items[i-1], items[i]
            i -= 1
    return items