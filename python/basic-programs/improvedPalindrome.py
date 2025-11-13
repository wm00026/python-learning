"""
This is an improve version of an earlier palindrome checking program.
It includes:
    - Handling of case sensitivity
    - Reading from a file
    - User-friendly output
Author: @wm00026
"""
# ======== function definitions ========
"""
function is_palindrome:
@brief: Checks if a word is a palindrome, ignoring case sensitivity.
@param word: String - the word to be checked.
@returns : String - The palindrome of the original word.
"""
def is_palindrome(word):
    normal_word = word.lower()
    palindrome = normal_word == normal_word[::-1]
    return palindrome


"""
function read_file:
@brief: Reads words from a file.
@param file_path: String - path to the file.
@returns: the words read from the file
"""
def read_file(file_path):
    # Reads word from a file
    with open(file_path, 'r') as file:
        words = file.readlines()
    return [word.strip() for word in words]


# Main function:
if '__main__' == __name__:
    choice = input("Do you want to read words from a file? (y/n): ").strip().lower()

    if choice == 'y':
        file_path = input("Enter the file path: ").strip()
        words = read_file(file_path)
    
    else:
        runs = input("Enter number of words to check: ")
        loops = int(runs)
        words = []
        for _ in range(loops):
            word = input("Enter a word: ")
            words.append(word)
    
    for word in words:
        if is_palindrome(word):
            print(f'"{word}" is a palindrome.')
        else:
            print(f'"{word}" is not a palindrome.')
# ======== end of main function ========