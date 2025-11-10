"""
This is a basic python program that prints "Hello, World". 
The amount of times "Hello, World" is printed is based off of an input from the user.

It utilizes the following important concepts:
    - Functions
    - Basic error checking
    - Type casting
    - For in range loops.
Author: wm00026
"""

"""
function print_hello_world:
@brief: Prints "Hello, World!" x number of times based on user input.
@param count: Integer - should be initialized to 0, used to count the number of times "Hello, World!" is printed.
@param number_str: String - user input that should represent a number.
@return: None
"""
def print_hello_world(count, number_str):
    if count != 0:
        print("Error: count must be zero")
        return

    count = 0
    
    if not number_str.isdigit():
        print("Error: The input should be a number.")
        return

    number = int(number_str)

    if number < 1:
        print("Error: Range number should be greater than zero")
        return

    for _ in range(number):
        print("Hello, World!")
        count += 1
    
    final_count = count

    print("Hello World was printed", final_count , "times!")
#=================================== end of function defintion =================================


#main function 
number_input = input("Type in a number: ")
print_hello_world(number_input)

