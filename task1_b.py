"""
Name: Benedita Victor Sarmento
Student NO: 24802248
Date: 25/10/2024

Task 1B: String Checker Program

This program defines a function that checks if a list of strings end with '.ac.uk', similar to how universities like University of Northampton
validates academic domain names. This program uses a simple loop to iterate through the list of strings and returns a list of boolean values 
that shows whether each string meets the rules.

1. define the function called ends_with_ac_uk to take a single parameter (strings)
2. provide docstring with examples and sample tests
3. initialize the variables:
        - "end" to hold the string: ac.uk
        - "result" as an empty list to store True/False 
4. loop through each string in the list with a for loop
5. check if the string ends with '.ac.uk'
6. return the "result" list
7. run tests with doctest 
"""

def ends_with_ac_uk(strings):
# this function checks if each string in the list ends with '.ac.uk'.
    """
    This function checks if each string in the list ends with '.ac.uk'.
    
    Example:
    >>> ends_with_ac_uk(["example.ac.uk", "example.com"])
    [True, False]
    >>> ends_with_ac_uk(["", "test", "example.ac.uk"])
    [False, False, True]
    >>> ends_with_ac_uk(["test.ac.uk", ".ac.uk", "test.ac.org"])
    [True, True, False]
    """
    # these examples are for the doctest and shows input and expected output
    end = '.ac.uk'
    # a variable is defined as "end" that holds the string '.ac.uk', which we are going to check against
    result = []
    # "result" is created as an empty list to store the boolean results of whether each string ends with '.ac.uk'
    
    for i in strings: # this loops through each string in the input list
        if i.endswith(end): # this checks if the current string ends with '.ac.uk'
            result.append(True) # if the string ends with '.ac.uk', True is added to the result list (I will also not that we have also JUST learned what .append() does in Week 5's online session)
        else:
            result.append(False) # if the string doesnt end with '.ac.uk', False is added to the result list
    return result # the function finally returns the reslt list whoch has the boolean values

if __name__ == "__main__":
    import doctest
    doctest.testmod()