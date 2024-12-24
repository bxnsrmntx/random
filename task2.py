"""
Name: Benedita Victor Sarmento
Student NO: 24802248
Date: 28/10/2024

Task 2: BMI Calculator with Categorization

I broke down the program in steps as follows:
1. start the program by defining the main function ('def main()').
2. check if the CSV file exists; if not, write the header (more detail in choosing os.path.isfile() and os.path.exists() below).
3. prompt the user for their name.
4. prompt the user for their weight in kilograms.
5. prompt the user for their height in centimeters.
6. convert height from centimeters to meters.
7. calculate the BMI using the formula: BMI = weight / (height in meters)².
8. determine the BMI category based on the calculated BMI.
9. create a formatted result string: name, weight, height, bmi, categorization.
10. open a CSV file in append mode and write the result to the file.
11. inform the user that the results have been saved.
12. call the main function to run the program.

This program uses a couple of materials that were not discussed in CSY1020's learning materials including:
- os.path.isfile() from Python's official documentation website (https://docs.python.org/3/library/os.path.html#module-os.path)
"""

import os  # import the os module for file operations

def main():  # define the main function
    bmi_file = "bmi.csv"  # define the name of the CSV file

    # check if the CSV file exists, and if not, write the header
    if not os.path.isfile(bmi_file):  # if the file does not exist
        with open(bmi_file, "w") as file:  # open the file in write mode
            file.write("Name,Weight (kg),Height (cm),BMI,Categorization\n")  # write the header

    # ask the user for their name
    while True: # loop until valid name is entered
        name = input("Enter your name: ").strip()  # get the name and get rid of any spaces
        if name and not name.isdigit():  # check if what user entered is no\t empty and not just digits
            break # exit loop if it is a valid name
        elif name.isdigit():  # check if the input is only digits
            print("Bro are you Elon Musk's kid? Please enter an actual name.")
        else:
            print("Dude, your name isnt supposed to be invisible")

    # ask the user for their weight in kilograms
    while True:  # loop until valid weight is entered
        weight_input = input("Enter your weight in kilograms (kg): ")
        if weight_input.replace('.', '', 1).isdigit():  # check if input is a valid number
            weight = float(weight_input) # converts the input to a float
            if weight > 0:
                break # exit loop if the weight is valid
            else:
                print("Dude, stop cosplaying as a speck of dust. Give me your actual weight.")
        else:
            print("Invalid!! Do you know what numbers are?")

    # ask the user for their height in centimeters
    while True:  # loop until valid height is entered
        height_input = input("Enter your height in centimeters (cm): ")
        if height_input.replace('.', '', 1).isdigit():  # check if input is a valid number
            heightcm = float(height_input)
            if heightcm > 0:
                break # exit the loop if the weight is valid
            else:
                print("You're either on the ground or under it with that number. Give me your actual height.")
        else:
            print("Invalid!! Do you know what numbers are?")

    # convert height from centimeters to meters
    heightm = heightcm / 100  # divide by 100 to get height in meters

    # calculate the BMI
    bmi = weight / (heightm ** 2)  # use the BMI formula

    # determine the BMI category
    if bmi < 18.5:  # check if BMI is underweight
        category = "underweight"
    elif 18.5 <= bmi < 25.0:  # check if BMI is healthy
        category = "healthy"
    elif 25.0 <= bmi < 30.0:  # check if BMI is overweight
        category = "overweight"
    else:  # if BMI is obese
        category = "obese"

    # create a formatted result string with units
    result = f"{name},{weight},{heightcm},{bmi:.2f},{category}"  # Prepare the output string

    # open a CSV file in append mode and write the result to the file
    with open(bmi_file, "a") as file:  # open the file in append mode
        file.write(result + "\n")  # write the result followed by a newline

    # inform the user that the results have been saved
    print("Your BMI has been calculated and saved to 'bmi.csv'.")  # Provide feedback to the user

# call the main function to run the program
if __name__ == "__main__":  # check if the script is being run directly
    main()  # call the main function