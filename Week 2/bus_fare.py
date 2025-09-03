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


# Write your code below:
(name, gender, age, is_student) = get_personal_info()
if gender == "M": label = "Mr."
else: label = "Ms."

if age <= 6:
    print(f"{name}, you can travel for free.")
elif age >= 60:
    print(f"{label} {name}, you can get concessionary fare for senior citizens.")
elif age > 6 and age < 60 and is_student:
    print(f"{label} {name}, you can get concessionary fare for students.")
else:
    print(f"{label} {name}, you need to pay full fare.")

# EXPECTED OUTCOME:
# Jack Ma, M, 4, no -- travel for free
# Bill Gates, M, 61, yes -- concession for senior
# Lim Hui Yan, F, 21, yes -- concession for students