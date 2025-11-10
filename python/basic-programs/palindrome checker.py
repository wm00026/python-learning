"""
A basic palindrome checker

Author: @wm00026
"""


"""
function palindrome_check:
@brief: Checks if a word is a palindrome.
@param word: String - the word to be checked.
@returns: None.
"""
def palindrome_check(word):
    
    if word == word[::-1]:
        print("Is a palindrome")
    else:
        print("Is not a palindrome")
# ======== end of function defintion ========



#main function:
runs = input("Enter a number: ")

loops = int(runs)

for _ in range(loops):
    word = input("Enter a word: ")
    palindrome_check(word)