'''Name: Tim Y.
Assignment: Password Validator
#Reflection: What you liked? Working with boolean values is cool.
    What you struggled with? The for loop dealing with the duplicate value lists
    How did you write your code to be efficient and reduce redundancy?
    I condensed the code and attempted to use the least amount of code possible.
    Share exactly 2 things that you learned on this assignment
    1. How to find duplicate values within a string using a for loop and lists
    2. How to use for loops effectively with lists
    '''

def getInitialsTY(name):
    sSplitTY = name.split() #split the string
    if len(sSplitTY) < 2: #data validation, allows user to enter 1 string or character or none
        return '' #return nothing and continue
    return sSplitTY[0][0].upper() + sSplitTY[1][0].upper() #return the first characters of the 2 strings
def main():
    sNameTY = input("Please enter first and last name: ") #user input
    sInitialsTY = getInitialsTY(sNameTY) #process user input and fetch initials through the function

    while True: #while loop for data validation
        duplicateChars = [] #lists for checking for duplicate characters
        duplicateCounts = []
        seenChars = []
        specialChars = ['!', '@', '#', '$', '%', '^']  # list for checking special characters

        sPasswordTY = input("Please enter password: ") #user input
        pwUpperTY = sPasswordTY.upper() #capitalize the input and store in a variable

        bLower = bUpper = bDigit = bSpecial = bLength = bInitial = False #initialize booleans used for validation
        bValid = bPass = True

        if sInitialsTY and sInitialsTY in pwUpperTY: #handle empty strings and check if user initials are within the string
            bInitial = True
            bValid = False
        if "PASS" in pwUpperTY: #check for string "pass"
            bPass = False
            bValid = False
        if len(sPasswordTY) < 8 or len(sPasswordTY) > 12: #verify password length
            bLength = True
            bValid = False
        for sCharacter in sPasswordTY: #string methods to check for numerics & characters
            if sCharacter.islower():   bLower = True
            if sCharacter.isupper():    bUpper = True
            if sCharacter.isdigit():    bDigit = True
            if sCharacter in specialChars: bSpecial = True #check special characters using the list
        for character in pwUpperTY: #check for duplicate characters
            if character not in seenChars: #if new character, append to seen characters
                seenChars.append(character)
                count = pwUpperTY.count(character) #count used to index how many duplicates are present
                if count > 1: #all duplicates get appended to the characters list and the count list
                    duplicateChars.append(character)
                    duplicateCounts.append(count)
        if duplicateChars: #if true
            print("These characters appear more than once: ")
            for i in range(len(duplicateChars)): #print the duplicate characters
                print(f"{duplicateChars[i]}: {duplicateCounts[i]} times")
            bValid = False
        if not bLower: #data validation
            print("Password must contain at least 1 lowercase letter.")
            bValid = False
        if not bUpper: #data validation
            print("Password must contain at least 1 uppercase letter.")
            bValid = False
        if not bDigit: #data validation
            print("Password must contain at least 1 digit.")
            bValid = False
        if not bPass: #data validation
            print("password cannot contain 'pass'")
            bValid = False
        if bLength: #data validation
            print("password length must be between 8 and 12 characters.")
        if bInitial: #data validation
            print("password cannot contain your initials.")
        if not bSpecial: #data validation
            print(f"password must contain at least 1 special character. {specialChars}")
            bValid = False
        if bValid: #if password is valid print validation message
            print('Password is valid and OK to use.')
            break


main()