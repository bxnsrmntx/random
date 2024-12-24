"""
Name: Benedita Victor Sarmento
Student NO: 24802248
Date: 25/10/2024

Task 1A: Lightyear to Kilometre Converter

This program converts a distance given in lightyears (LY) to kilometres (KM) using the formula:
KM = LY / 0.00000000000010570.

This program uses a couple of materials that were not discussed in CSY1020's learning materials including:
- try and except (ValueError)
- .strip()
- .lower()
"""

while True:
# loop asks user to input a value of LY using try and except from Python's official documentation on how to handle exceptions (https://docs.python.org/3/tutorial/errors.html)
    try: 
    #  the try block allows to attempt the conversion and only handle errors when they occur without the need to write multiple conditional checks for if-else
        ly = float(input("Enter a value of Light Year: ")) 
        # uses float instead of int to make sure that is can handle wider range of values and can provide more accurate result
        km = ly / 0.00000000000010570
        print((f"{ly} lightyears is equal to {km} km"))
    except ValueError: # user is asked to type in proper value if they input a value that cannot be converted into a float (string/char)
        print("Please enter a valid number!! >:(")
        continue
    
    again = input("Do you want to use the LY to KM converter again? (yes/no or y/n): ").strip().lower() 
    # uses '.strip()' to remove leading or trailing space ex: " yes " = "yes"; learned from Python's official documentation on std types (https://docs.python.org/3/library/stdtypes.html#str.strip)
    # uses '.lower()' to convert user input to lowercase to prevent the use of multiple unnecessary values in the list ex: "YES" = "yes"
    if again not in ['yes', 'y']: #uses 'not in' instead of == to check to nullify the need to write multiple == checks and allows for adding more accepted responses by modifying the list
        break # if user enters anything other than a y or yes, the loop stops and jumps to print the last line
print("Thank you for using the lightyear to kilometre converter, peace out :)")