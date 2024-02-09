# Lab 1 Group 8
# Patrick Hollyer-Viggiani and Manish Singh
# January 26, 2024
# Random Password Generator
# Description: Creating a program that can generate a random passwor for the user, based on the user's specific paramaters

# Importing tha random and string library create random letters/numbers
import random
import string

def r_calc(pw_length, numletters, numdigits, numspecial):
    
    try:
        int(pw_length)
        if pw_length > 8:
            pass
        else:
            print("Please enter a number greater than 8.")
    except:
        print("Please enter a number greater than 8.")
    
    try:
        int(numletters)
        if numletters >= 0 and numletters <= pw_length:
            newlen1 = pw_length - numletters
        else:
            print(f"Please enter a number from 0 to {pw_length} for letters")
    except:
        print(f"Please enter a valid number for letters.")

    
    
    try:
        int(numdigits)
        if numdigits >= 0 and numdigits <= newlen1:
            newlen2 = newlen1 - numdigits
        else:
            print(f"Please enter a number from 0 to {newlen1} for numbers")
    except:
        print(f"Please enter a valid number for numbers.")

    
    
    try:
        int(numspecial)
        if numspecial == newlen2:
            for validinputs in range(1):
                password = []

                # Storing random letters as a variable
                chars = string.ascii_letters
                # Storing random numbers as a variable
                digits = string.digits
                # Storing random special characters as a variable
                spec_chars = string.punctuation

                # Iterate through letters the amount of times as user input
                for letters in range(numletters):
                    # Store values as variable
                    char_amount = random.choice(chars)
                    # Add letters to the list
                    password.append(char_amount)
                
                # Iterate through letters the amount of times as user input
                for nums in range(numdigits):
                    # Store values as variable
                    num_amount = random.choice(digits)
                    # Add numbers to the list
                    password.append(num_amount)
                
                # Iterate through letters the amount of times as user input
                for punct in range(numspecial):
                    # Store values as variable
                    punct_amount = random.choice(spec_chars)
                    # Add special characters to the list
                    password.append(punct_amount)

                # Shuffling the list to make the order random
                random.shuffle(password)
                
                # Joining the list together to make it a string
                password1 = "".join(password)

                #Printing new password
                print(f"Your new password is {password1}")
        else:
            print(f"Please enter {newlen2} special characters to finish the password.")
    except:
        print(f"Please enter a valid number for special characters.")
    
r_calc(10,4,3,asd)