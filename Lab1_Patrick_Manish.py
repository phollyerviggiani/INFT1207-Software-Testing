# Lab 1 Group 8
# Patrick Hollyer-Viggiani and Manish Singh
# January 27, 2024
# Random Password Generator
# Description: Creating a program that can generate a random password for the user, based on the user's specific paramaters

# Importing tha random and string library create random letters/numbers
import random
import string


# Function for password generator
def password_generator():

    # Setting condition of while loop to false to start the loop
    validloop = False

    # Start of the loop
    while validloop == False:
        # Trying to cast input as an int
        try:
            pwlength = int(input("Please enter the length of your password: "))
            # If input is valid, end the loop and store the data in cariable pwlength
            if pwlength >= 8:
                validloop = True

            # If input is invalid, repromt user for input
            else:
                print("Please enter a number greater or equal to 8.")

        # If input is invalid, repromt user for input
        except:
            print("Please enter a valid number.")

    # Setting condition of while loop to false to start the loop    
    validloop = False

    # Start of the loop
    while validloop == False:
        # Trying to cast input as an int
        try:
            charlength = int(input("Please enter the number of letters: "))
            # Checking to see if input is >= 0, and less than the password length, store input as charlength
            if charlength >= 0 and charlength <= pwlength:
                
                # Counter to keep track of available numbers
                remainder = pwlength - charlength
                # Printing numbers of digits left total, and how many you can use for the next section
                print(f"You have {remainder} digits remaining.")
                # Exiting the loop
                validloop = True

            # If input is above the number of digits you can use for this section, print the following    
            else:
                print(f"The number of letters should be in the range of 0 and {pwlength}.")

        # If input is invalid, repromt user for input
        except:
            print("Please enter a valid number.")

    
    # Setting condition of while loop to false to start the loop 
    validloop = False

    # Start of the loop
    while validloop == False:
        # Trying to cast input as an int
        try:
            numlength = int(input("Please enter the amount of numbers: "))
            # If input is >= 0 and less than the remaining digits for password, store value as numlength
            if numlength >= 0 and numlength <= remainder:
                # Store remaining numbers required in the list as leftovers
                leftovers = remainder - numlength
                # Display remaining digits 
                print(f"You have {leftovers} digits left to choose from")
                # Exit the loop
                validloop = True

            # If digits are less than 0 and higher than leftover digits remaining, display the following    
            else: 
                print(f"The number of digits should be in the range of 0 and {remainder}.")
        
        # If input is invald, display the following
        except:
            print("Please enter a valid number.")

    
    # Setting condition of while loop to false to start the loop
    validloop = False
    # Start of the loop
    while validloop == False:
        # Trying to cast input as an int
        try:
            specialchar = int(input("Please enter the number of special characters: "))
            # If input is above 0 and equal to remaining digits, store input
            if numlength >= 0 and specialchar == leftovers:
                # Exit the loop
                validloop = True

            # If input is below or above remaining digits, print the following
            else:
                print(f"You need to enter {leftovers} to complete the password.")

        # If input is invalud, display the following    
        except:
            print("Please enter a valid number.")
        
    # Creating an empty list called password
    password = []

    # Storing random letters as a variable
    chars = string.ascii_letters
    # Storing random numbers as a variable
    digits = string.digits
    # Storing random special characters as a variable
    spec_chars = string.punctuation

    # Iterate through letters the amount of times as user input
    for letters in range(charlength):
        # Store random values as variable
        char_amount = random.choice(chars)
        # Add letters to the list
        password.append(char_amount)
    
    # Iterate through letters the amount of times as user input
    for nums in range(numlength):
        # Store random values as variable
        num_amount = random.choice(digits)
        # Add numbers to the list
        password.append(num_amount)
    
    # Iterate through letters the amount of times as user input
    for punct in range(specialchar):
        # Store random values as variable
        punct_amount = random.choice(spec_chars)
        # Add special characters to the list
        password.append(punct_amount)

    # Shuffling the list to make the order random
    random.shuffle(password)
    
    # Joining the list together to make it a string
    new_password = "".join(password)

    #Printing new password
    print(f"Your new password is {new_password}")
    
# Calling the function
password_generator()