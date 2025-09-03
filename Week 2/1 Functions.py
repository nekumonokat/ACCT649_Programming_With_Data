# Q1: Functions for Numbers
# a. calculates the average of 3 numbers
def compute_average():
    one = float(input("Enter 1st number: "))
    two = float(input("Enter 2nd number: "))
    three = float(input("Enter 3rd number: "))
    print("Average:", (one + two + three)/3)

# compute_average()
# EXPECTED OUTCOME
# Enter 1st number: 23.9
# Enter 2nd number: 198.3
# Enter 3rd number: -95.7
# Average: 42.16666666666667

# b. calculate geometric mean
def compute_geometric_mean(x, y, z):
    output = (x*y*z)**(1/3)
    print(f"The geometric mean of {x}, {y} and {z} is: {output}")

# compute_geometric_mean(2, 4, 6)
# EXPECTED OUTCOME
# The geometric mean of 2, 4 and 6 is: 3.634241185664279



# Q2: Message Printer
def print_a_line():
    print("-"*20)

def print_a_message(msg, sym):
    # print(x)
    # MODIFIED TO ALLOW STORING OF VALUE
    x = sym + " " + msg + " " + sym
    return x

# print_a_line()
# print_a_message("Hello SIS!", "|")
# print_a_line()
# print_a_line()
# print_a_message("Hello Python!", "*")
# print_a_message("Hello Functions!", "$")
# print_a_line()



# Q3: Signage Printer
import lab1_q3_helper as q3

def print_signage(msg, sym):
    msg_ = print_a_message(msg, sym)
    q3.print_a_customized_line(sym, len(msg_))
    print(msg_)
    q3.print_a_customized_line(sym, len(msg_))

# print_signage("Hello!", "*")
# print_signage("Welcome to SMU", "#")



# Q4: Python Standard Libraries
# a. cm^2 to cm
import math
def q4a():
    val = float(input("What's the size of the square (in square centimeters)? "))
    print(f"Each side of this square is {math.sqrt(val)} centimeters.")

# q4a()

# b. random integer
import random
def q4b():
    n = int(input("Enter a positive integer: "))
    print(random.randint(1, n))

# q4b()



# Q5: Importing a Module
# DONE ON lab1_insurance.py



# Q6: Time Calculator
def sys_time():
    # DEFINING CONSTANTS:
    SECS_PER_MIN = 60
    MINS_PER_HR = 60
    HRS_PER_DAY = 24
    SECS_PER_HR = 60 * SECS_PER_MIN
    SECS_PER_DAY = SECS_PER_HR * HRS_PER_DAY

    secs = int(input("Please enter the system time (in seconds): "))
    days = secs // (SECS_PER_DAY)
    secs %= (SECS_PER_DAY)
    hours = secs // (SECS_PER_HR)
    secs %= (SECS_PER_HR)
    mins = secs // SECS_PER_MIN
    secs %= SECS_PER_MIN
    print(f"Based on this system time, {days} days, {hours} hours, {mins} minutes and {secs} seconds have passed since 1 January 1970 00:00:00 UT.")

# sys_time()
# EXPECTED OUTCOME
# Please enter the system time (in seconds): 266460
# Based on this system time, 3 days, 2 hours, 1 minutes and 0 seconds have passed since 1 January 1970 00:00:00 UT.



# Q7: Tax Calculator
# COMMENT: THIS QUESTION WAS DONE IN OTHER EXERCISE WITH IF STATEMENTS
# a. calculate tax - 20000 - 30000
def calculate_tax_1(income):
    # returns total tax needed to pay
    print((income - 20000) * 0.02)
    
# calculate_tax_1(25000)

# b. more flexible calculate tax - 0 - 30000
def calculate_tax_2(income):
    # returns total tax needed to pay
    # use max to prevent negative numbers - had to check online to get hints
    taxables = max(income - 20000, 0)
    print(taxables * 0.02)

# calculate_tax_2(25000)
# calculate_tax_2(10000)

# c. improved calculate tax - 0 - 40000
def calculate_tax_3(income):
    rem = income
    total = 0
    thresh30 = max(rem - 20000, 0) # income - 20000
    thresh40 = max(thresh30 - 10000, 0) # income - 30000
    taxables_30 = thresh30 - thresh40
    taxables_40 = thresh40
    total += taxables_30 * 0.02
    total += taxables_40 * 0.035
    print(total)

# calculate_tax_3(25000)
# calculate_tax_3(10000)
# calculate_tax_3(35000)

# d. finalised calculate tax
def calculate_tax_4(income):

    # CONSTANTS
    THRESHOLDS = (20000, 30000, 40000, 80000, 120000, 160000, 200000, 240000, 280000, 320000)
    TAX_RATES = (2, 3.5, 7, 11.5, 15, 18, 19, 19.5, 20, 22)

    thresh30 = max(income - THRESHOLDS[0], 0) # salary - 20000
    thresh40 = max(income - THRESHOLDS[1], 0) # salary - 30000
    thresh80 = max(income - THRESHOLDS[2], 0) # salary - 40000
    thresh120 = max(income - THRESHOLDS[3], 0) # salary - 80000
    thresh160 = max(income - THRESHOLDS[4], 0) # salary - 120000
    thresh200 = max(income - THRESHOLDS[5], 0) # salary - 160000
    thresh240 = max(income - THRESHOLDS[6], 0) # salary - 200000
    thresh280 = max(income - THRESHOLDS[7], 0) # salary - 240000
    thresh320 = max(income - THRESHOLDS[8], 0) # salary - 280000
    excess = max(income - THRESHOLDS[9], 0) # salary - 320000

    thresh30 -= thresh40
    thresh40 -= thresh80
    thresh80 -= thresh120
    thresh120 -= thresh160
    thresh160 -= thresh200
    thresh200 -= thresh240
    thresh240 -= thresh280
    thresh280 -= thresh320
    thresh320 -= excess

    total = (
                thresh30 * TAX_RATES[0]/100 +
                thresh40 * TAX_RATES[1]/100 +
                thresh80 * TAX_RATES[2]/100 +
                thresh120 * TAX_RATES[3]/100 +
                thresh160 * TAX_RATES[4]/100 +
                thresh200 * TAX_RATES[5]/100 +
                thresh240 * TAX_RATES[6]/100 +
                thresh280 * TAX_RATES[7]/100 +
                thresh320 * TAX_RATES[8]/100 +
                excess * TAX_RATES[9]/100
              )
    
    print(total)

calculate_tax_4(25000)
calculate_tax_4(10000)
calculate_tax_4(35000)
calculate_tax_4(350000)