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

def print_hello_world(number_str):

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
#================================================

number_input = input("Type in a number: ")
print_hello_world(number_input)

