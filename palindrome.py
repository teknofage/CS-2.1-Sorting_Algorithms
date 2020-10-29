#TODO: write a recursive version of ispalindrome
def is_palindrome_iterative(my_string):
    
    left = 0
    right = len(my_string) -1
    
    while left <= right:
        if my_string[left] != my_string[right]:
            return False
        left += 1
        right += 1
        
print(is_palindrome_iterative("tacocat")) #should print True
print(is_palindrome_iterative("hello"))#should print False
        

def ispalindrome(my_string, left, right):


    if left == right:
        return True
    if my_string[left] != my_string[right]:
        return False
   
    else:
        return True


print(ispalindrome("tacocat"), 0, len("tacocat") - 1) #should print True
print(ispalindrome("hello"), 0, len("hello") -1)#should print False


