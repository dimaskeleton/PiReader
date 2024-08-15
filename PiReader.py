"""
Contract: Read and process the first million digits of pi in the given .txt file
Purpose:
    - Read the given file
    - Calculate the frequency of each digit
    - Search for a given sequence of digits in the file
    - Remove a given digit and save the result into a new txt file
"""

'''
Reads and returns contents of the given file 
'''


def read_file(filename="pi_million_digits.txt"):
    try:
        with open(filename, 'r') as pi_file:  # Open the file for reading
            pi_digits = pi_file.read()  # Read the entire contents of the file
        return pi_digits  # returns the contents of the file

    except FileNotFoundError:
        print("the file was not found")  # Error message if the file isn't found or doesn't exist
        return "The file was not found"  # Returns the error message


'''
Calculates and returns the frequency of each digit in the given string 
'''


def digit_frequency(pi_digits):
    # Initialize frequency count for each digit
    frequency = {str(digit): 0 for digit in range(10)}

    # Counts the frequency of each digit
    for char in pi_digits:
        if char.isdigit():
            frequency[char] += 1

    # Print the frequency of each digit
    print("Frequency of each digit in the pi digits:")
    for digit in range(10):
        print(f"{digit}: {frequency[str(digit)]}")

    # Return the frequency dictionary
    return frequency


'''
Searches for a sequence of digits within the given string and returns it's position if found
'''


def digit_search(pi_digits, sequence):
    # Find the position of the sequence
    position = pi_digits.find(sequence)

    # uses .find func to find the sequence in the string, if sequence isn't found it returns -1
    # if position is not -1, returns the sequenced searched and it's position
    if position != -1:
        print(f"The sequence {sequence} was found at position {position} in the pi digits.")
        return f"The sequence {sequence} was found at position {position} in the pi digits."

    # if sequence isn't found, returns -1 and outputs that the sequence wasn't found
    else:
        print(f"The sequence {sequence} was not found in the pi digits.")
        return f"The sequence {sequence} was not found in the pi digits."


'''
Removes all occurrences of a given digit from the string and exports the result into a new txt file 
'''


def remove_digit(pi_digits, remove_digit, export_file):
    # Remove the specified digit, replacing it with ""
    new_digits = pi_digits.replace(remove_digit, "")

    # Opens the export_file for writing
    with open(export_file, 'w') as file:
        # Writes the new, updated digits to the file
        file.write(new_digits)

    # Print and return the result of removing a digit
    print(f"Updated pi digits with all {remove_digit} removed and saved to {export_file}")
    return f"Updated pi digits with all {remove_digit} removed and saved to {export_file}"


'''
Calls all the functions listed above with given parameters to test and see if it's working 
'''


def call_all_functions():
    # Calling read_rile() and printing the file contents
    pi_digits = read_file()
    print(f"The following are the first million digits in pi {pi_digits}")

    # Calling digit_frequency to see the frequency of every digit
    digit_frequency(pi_digits)

    # Calling digit search to see if/where a sequence of number occurs
    digit_search(pi_digits, ".14")
    digit_search(pi_digits, "458151")
    digit_search(pi_digits, "447850")
    digit_search(pi_digits, "101010")
    digit_search(pi_digits, "839363")

    # Calling remove_digit to remove the given digit
    remove_digit(pi_digits, "8", "pi_removed_digit.txt")


call_all_functions()

