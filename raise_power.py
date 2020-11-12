"""Reasonable test inputs: 
integer = x = 5
power = n = 3

Pseudocode:
Create function
Create If statement
Create base case where the power is equal to 1,
and therefore the answer is equal to the integer.
Create recursive case, where the integer is 
multiplied by the function raise_power recursively, or in other
words, it is multiplied by itself n-1 times.
"""

def raise_power(x, n):
    # base case: if power (n) is equal to 1, 
    if n == 1:
        # return integer (x)
        return x
    else:
        # otherwise multiply x by raise_power() 
        # recursively x, n-1 times, which is the same 
        # as raising it by the power of n, 
        # and return the result
        return x * raise_power(x, n-1)
    
print(raise_power(5,3))

def test_raise_power():
    if raise_power(4,2) == 16:
        print("The test works!")
        return True
    else:
        print("The test does not work!")
        return False
    
test_raise_power()