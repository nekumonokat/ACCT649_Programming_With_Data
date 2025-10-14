# The following function is provided to you.
# Do not modify the function definition!
def get_personal_info():
    """
    This function prompts the user for his/her name, gender, age and whether
    or not he/she is a student.
    The function returns a tuple that contains all the information entered
    by the user.
    """
    name = input("What's your name? ")
    gender = input("What's your gender? [M|F] ")
    age = int(input("What's your age? "))
    is_student = input("Are you a student? [yes|no] ")
    return (name, gender, age, is_student == 'yes')


# Use function above to get user info, which returns a tuple
result = get_personal_info()

# Store values of tuples into variables
name = result[0]
gender = result[1]
age = result[2]
is_student = result[3]

# If 6 years or younger
if age <= 6:
    print(name + ", you can travel for free.")
    
# Else, print title and name first depending on gender
else:
    if gender == "M":
        print("Mr. " + name, end="")
    elif gender == "F":
        print("Ms. " + name, end="")
    
    # Now print rest depending on age and whether they are student or not
    if age >= 60:
        print(", you can get concessionary fare for senior citizens.")
    elif is_student:
        print(", you can get concessionary fare for students.")
    else:        
        print(", you need to pay full fare.")
    