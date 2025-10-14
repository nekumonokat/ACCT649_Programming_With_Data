# To run this program:
#   1) Open a new Anaconda prompt
#   2) Use "cd" command to go to correct folder (e.g. "cd OneDrive - Singapore Management University", etc.)
#   3) Type "python lab1_insurance.py" 


# This allows us to use the function that we wrote in lab1_utility.py
import lab1_utility

# Prompt user for their info
age = int(input("What's your age? "))
print()
gender = input("What's your gender [M/F]? ")

# Use function to determine premium
premium = lab1_utility.get_insurance_premium(age, gender)
print("Your premium is " + str(premium))