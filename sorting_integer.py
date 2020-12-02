#!python
from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO:   Running time: 
                O(n+k)
            Why and under what conditions?
                It is always linear but, its complexity will be equal to how many 
                times the body of inner cycle is executed.
    TODO:   Memory usage: 
                O(k)
            Why and under what conditions?
                Under the worst conditions, because it only creates one extra data structure
            """
     
    # Create output variable and set it to equal length of numbers array that will be sorted  
    output = [0 for i in range(len(numbers))] 
  
    # Create a count array to store count of individual characters and initialize 
    # count array as 0 
    count = [0 for i in range(256)] 
  
    # ans variable for storing the resulting answer since the  
    # string is immutable 
    ans = ["" for _ in numbers] 
  
    # for each character, use ord to return the unicode code of the character
    for i in numbers: 
        # increment the ord index count 
        count[ord(i)] += 1
  
    # Change count[i] so that count[i] now contains actual 
    # position of this character in output array 
    for i in range(256): 
        count[i] += count[i-1] 
        
    # for each character, use ord to return the  
    # Build the output character array 
    for i in range(len(numbers)):
        # Create list of counts with a slot for each number in input range
        # Loop over counts and append that many numbers into output list
        output[count[ord(numbers[i])]-1] = numbers[i] 
        count[ord(numbers[i])] -= 1
  
    # Traverse the length of numbers array. Copy the output array to numbers, 
    # so that arr now contains sorted characters 
    for i in range(len(numbers)): 
        ans[i] = output[i] 
    return ans  
  
# Input to test counting_sort function 
# numbers = "canyourearrangeme"
# numbers = "76564231469234"
# ans = counting_sort(numbers) 
# print("Sorted character array is % s" %("".join(ans))) 


# input = [1,5,6,7,8,4,5,7,6,4]
# output = []
#     # use the equation given to determine which region of the buckets we need to put the index in
# def equation(input, num_buckets, index):
#     len(input) * input(index) / len(input) + 1
#     # loop through input
#     for i in range(len(input)):
#     # if the result of the equation does not equal 0
#         if len(output[equation(input, num_buckets, input[i])]) != 0:
#         # append it to the output
#             output[equation(input, num_buckets, input[i])].append(input[1])
#         return print(output)


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
#     then sorting each bucket and concatenating all buckets in sorted order.
#        Running time: 
#                 Best: 0(n*k) 
#             Why and under what conditions?
#                 You only need to traverse the original array once, 
#                 and the new array or buckets k times, where k is the number of 
#                 buckets that are not empty.
                
#                 Worst: 0(n^2) 
#             Why and under what conditions?
#                 There would be the same number of full buckets as there are 
#                 items in the original array, or else the array values are so unevenly 
#                 distributed that the sorting and arranging of the sub-arrays in
#                 the buckets takes up a lot of time
#        Memory usage: 
#                 0(n) 
#             Why and under what conditions?
#                 Memory usage is minimal and linear, even under the worst 
#                 conditions, as the algorithm only needs 
#                 to create one extra data structure in the 
#                 form of the array of arrays, and in python
#                 these are all dynamic arrays which have flexible space.
#             """
    buckets = []

    # Create empty buckets
    for i in range(num_buckets):
        buckets.append([])

    # isnert each elements from numbers into each bucket
    for num in numbers:
        if type(num) is int:
            index = int(int(num/int(max(numbers)))* int((num_buckets - 1)))
            bucket = buckets[index]
            bucket.append(num)
        else:
            index = ((int(num)/int(max(numbers)))* ((num_buckets - 1)))
            bucket = buckets[index]
            bucket.append(num)

    # Then sort each element using insertion sort
    for bucket in buckets:
        insertion_sort(bucket)

    # get sorted elements
    k = 0
    for i in range(num_buckets):
        for value in buckets[i]:
            numbers[k] = value
            k += 1

    # return sorted numbers array
    return numbers


