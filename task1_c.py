"""
Name: Benedita Victor Sarmento
Student NO: 24802248
Date: 28/10/2024

Task 1C: Top-Down Algorithm Design
1. first step is to start the program
2. ask the user to input a series of single-digit numbers with nothing separating them
3. store the user's input in a variable
4. initialize a variable to hold the sum, starting at zero
5. loop through each character in the user's input (check if char is digit, then convert the character to int and add int value to the sum variable)
6. after loop, display the result (total sum)
7. finally end program
"""

def get_input():
    """this function asks the user for a series of single-digit numbers"""
    return input("Enter a series of single-digit numbers with no separators please > ")

def initialize_sum():
    """this initializes and returns the sum variable."""
    return 0

def calculate_sum(num):
    """this function calculates the sum of the digits in the input string."""
    total = 0 # initializes a variable to hold the sum starting at zero (step 4)
    for i in num:
        if i.isdigit(): # makes sure that only numeric characters from the user's input are processed
            total += int(i)
    return total

def display_result(total):
    """this function prints and displays the result to the user."""
    print(f"The sum of the numbers entered is: {total}")

def main():
    """this is the main function to run the program."""
    num = get_input() # call this function to get the user's input
    total_sum = calculate_sum(num) # calls this function to calculate the sum
    display_result(total_sum) # calls this function to display the result

# starts the program
if __name__ == "__main__":
    main()