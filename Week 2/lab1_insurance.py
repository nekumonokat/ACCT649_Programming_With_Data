import lab1_utility as ut

age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
print(ut.get_insurance_premium(age, gender))