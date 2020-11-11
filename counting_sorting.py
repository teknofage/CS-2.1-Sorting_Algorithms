def counting_sort(numbers):
    numbers = [3,2,5,3]
    new_array = [0] * (max(numbers) + 1)
    print("new array: ", new_array)
    for num in numbers:
        if new_array[num] == 0:
            new_array[num] = 1
        else:
            new_array[num] += 1
        print("new array: ", new_array)
        final = []
        for num in range(len(new_array)):
            if new_array[num] != 0:
                for x in range(new_array[num]):
                    final.append(num)
    return print("final array: ", final)
    
numbers = [3,2,5,3]        
counting_sort(numbers)