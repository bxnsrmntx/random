"""
Name: Benedita Victor Sarmento
Student NO: 24802248
Date: 04/11/2024

Task 3: Text File Statistics Code

This program analyzes a given text file (machine-stops.txt) and provides:
1. the total number of words in the file (labeled as tokens)
2. the frequency of a specific word
3. the normalized frequency of a specific word
4. the total number of sentences in the file
5. sentences that contain a specific word
"""

import os

def readFile(filename):
    """this function reads the content of the file and returns it if it exists."""
    if not os.path.isfile(filename):  # check if the file exists
        print(f"Woops! the file '{filename}' wasn't found!")  # print an error message if the file is not found
        return None  # return None if the file doesn't exist
    with open(filename, 'r', encoding='utf-8') as file:  # open the file in read mode with UTF-8 encoding
        return file.read()  # return the content of the file

def countTokens(filename):
    """this function counts the total number of words in the file."""
    text = readFile(filename)  # read the file content
    if text is None:  # check if the text is None (file not found)
        return 0  # return 0 if the file doesn't exist
    tokens = text.split()  # split the text into words using whitespace
    return len(tokens)  # return the number of words (tokens)

def countToken(filename, token):
    """this function counts how many times a specific word appears in the file."""
    text = readFile(filename)  # read the file content
    if text is None:  # check if the text is None (file not found)
        return 0  # return 0 if the file doesn't exist
    tokens = text.lower().split()  # convert text to lowercase and split into words
    return tokens.count(token.lower())  # return the count of the specified word ignoring case

def normalizedFrequency(filename, token):
    """this function calculates the normalized frequency of a specific word."""
    total_tokens = countTokens(filename)  # get the total number of words
    if total_tokens == 0:  # check if there are no words
        return 0  # return 0 to avoid division by zero
    token_count = countToken(filename, token)  # get the count of the specific word
    return token_count / total_tokens  # return the normalized frequency

def sentenceCount(filename):
    """this function counts the number of sentences in the file."""
    text = readFile(filename)  # read the file content
    if text is None:  # check if the text is None (file not found)
        return 0  # return 0 if the file doesn't exist
    sentences = text.split('.')  # split the text into sentences using periods
    return len([s for s in sentences if s.strip()])  # return the count of non-empty sentences

def sentencesContaining(filename, token):
    """this function finds sentences that contain a specific word."""
    text = readFile(filename)  # read the file content
    if text is None:  # check if the text is None (file not found)
        return []  # return an empty list if the file doesn't exist
    sentences = text.split('.')  # split the text into sentences using periods
    token_lower = token.lower()  # convert the token to lowercase for comparison (ignore case)
    matching_sentences = [s.strip() for s in sentences if token_lower in s.lower()]  # find and strip sentences containing the token
    return matching_sentences  # return the list of matching sentences

def main():
    # ask the user for the filename and keep asking until a valid file is provided
    while True:  # start an infinite loop
        filename = input("Enter the name of the text file (including .txt): ")  # prompt for filename
        text = readFile(filename)  # use readFile to check if the file exists and get its content
        if text is not None:  # if readFile returns content (file exists)
            break  # exit the loop if the file is valid
        else:
            print("Please try again :P")  # prompt the user to try again without repeating "file not found" message

    # display statistics using the functions
    total_tokens = countTokens(filename)  # get the total word count
    print("Total words (tokens):", total_tokens)  # print the total word count

    while True:  # loop for word searching
        token_to_search = input("Enter a word to search for: ").strip()  # ask for a word to search
        if not token_to_search or token_to_search.isspace() or token_to_search.isdigit(): # check if the token is invalid (number, empty, or whitespace only)
            print("Hey!! Please provide an actual valid word to search for >:(")
            continue # this ensures we skip the rest of the loop when the token is invalid
        
        frequency = countToken(filename, token_to_search)  # count the frequency of the word

        # if the frequency is 0 (invalid token), we should continue the loop
        if frequency == 0:
            # print the message if a valid token is entered but not found in the file
            print(f"The word '{token_to_search}' wasn't found in the file, damn. Type properly man")
            continue  # ask the user for a new word after printing the error message

        print(f"Normalized frequency of the word '{token_to_search}':", normalizedFrequency(filename, token_to_search))  # print normalized frequency
        print(f"Frequency of the word '{token_to_search}': ", frequency)  # print the frequency of the word
        
        sentences = sentencesContaining(filename, token_to_search)  # get sentences containing the word
        # if no sentences are found, skip the sentence printing
        if sentences:
            print(f"Sentences containing the word '{token_to_search}':")  # prompt to show sentences containing the word
            for sentence in sentences:  # loop through the matching sentences
                print("*", sentence)  # print each sentence
        break  # exit the loop after successfully finding the word
    print("Total sentences in the file:", sentenceCount(filename))  # print the total sentence count

if __name__ == "__main__":
    main()  # run the main function