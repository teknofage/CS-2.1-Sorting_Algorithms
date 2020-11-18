#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO:   Running time: 
                O(n+k)
            Why and under what conditions?
                It is always linear because ...
    TODO:   Memory usage: 
                O(k)
            Why and under what conditions?
                Under the worst conditions, 
            """
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
       Running time: 
                Best: 0(n*k) 
            Why and under what conditions?
                You only need to traverse the original array once, 
                and the new array or buckets k times, where k is the number of 
                buckets that are not empty.
                
                Worst: 0(n^2) 
            Why and under what conditions?
                There would be the same number of full buckets as there are 
                items in the original array, or else the array values are so unevenly 
                distributed that the sorting and arranging of the sub-arrays in
                the buckets takes up a lot of time
       Memory usage: 
                0(n) 
            Why and under what conditions?
                Memory usage is minimal and linear, even under the worst 
                conditions, as the algorithm only needs 
                to create one extra data structure in the 
                form of the array of arrays, and in python
                these are all dynamic arrays which have flexible space.
            """
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    input = [1,5,6,7,8,4,5,76,4]
    output = []
    
    def equation(index):
        len(input) * input(index) / len(input) + 1
        
    for i in input:
        if len(output[equation(input[i])]) != 0:
            output[equation(input[i])].append(input[1])
    return print(output)