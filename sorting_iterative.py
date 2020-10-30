#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(1)    
    Why and under what conditions? Not running through any loops and it uses a constant time.
    Memory usage: O(1)    
    Why and under what conditions? No new structures are created or changed so the memory usage is linear."""
    # make a copy of [sliced]items, sort it, and return True if copy matches items
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
    # set is_sorted status to True
    is_sorted = True
    # create a counter, set to 0
    counter = 0
    while(is_sorted):
        # while items is_sorted, set is_sorted to False
        is_sorted = False
        # then loop through items
        for i in range(len(items) - counter - 1):
            # if an item is larger than the one to the right of it...
            if items[i] > items[i+1]:
                # then they swap places
                items[i], items[i+1] = items[i+1], items[i]
                # and then they become sorted!
                is_sorted = True
        # increment the counter to move through the array
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

items = [3, 1, 41, 59, 26, 53, 59]
print(items)
selection_sort(items)

# print the list after we run Selection Sort
print(items)


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: Best: O(n), Average: O(n^2), Worst: O(n^2)      
    Why and under what conditions?  Best case only requires linear run time due to small list of items, and Worst case would use a large list of items.
    Memory usage: O(1)            
    Why and under what conditions? No new structures are created or changed so memory usage is minimal. """
    # set item_length to the range between 1 and length of items
    item_length = range(1, len(items))
    # loop through item_length
    for i in item_length:
        # item[i] values start as unsorted values
        unsorted_value = items[i]
        # while the item[-1] values are greater than the unsorted [i] value AND i is greater than 0
        while items[i-1] > unsorted_value and i > 0:
            # swap the location of the two items
            items[i], items[i-1] = items[i-1], items[i]
            # decrement i
            i -= 1
    return items