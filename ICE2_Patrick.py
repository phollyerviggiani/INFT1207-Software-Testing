# INFT1207 Software Testing and Automation
# ICE2 Fundamentals of Testing
# Patrick Hollyer-Viggiani 100910706
# Description: Write a program that tests the user's various inputs, displays said input, and prints the
#              lowest minimum input to the user. The input cannot be str/float, must be an int.


def get_input(): # input function
    while True:
        try:
            elements = input("Enter elements separated by space: ")
            elements_list = [int(ele) for ele in elements.split()] # gets the inputs, puts in list as int
            return elements_list
        except ValueError:
            print("Error! Please enter an int only.") # if invalid input, display the following

def minimum(elements): #function to find min input
    if not elements:
        raise ValueError("Cannot have an empty list.") # if empty list, display the following
    
    min = elements[0] # finding min element without the .min() function
    for element in elements:
        if element < min:
            min = element
    return min # returning the value

def run(): # function that will be called/run the other functions
    try:
        elements = get_input() # elements as the get_input() function
        minimum_element = minimum(elements) # minimum_element as minimum funciton, with parameters of elements
        print(f"The smallest number is: {minimum_element}") # printing the min value for user
    except ValueError:
        print("Cannot have an empty list.")
run() # calling the function to run