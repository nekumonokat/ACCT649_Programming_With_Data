# 1 Meter Fare
# - Flag-Down Fare
# - Fare based on distance rate

# Notes:
# - First 1km: flag-down fare
# - 1km - 9.8km: additional beyond 1km based on rate per 400m
# - Beyond 9.8km: additional rate per 350m

# 2 Surcharges
# - Time-Based Surcharges
# - Location Surcharges

# Notes:
# - Peak period: time-based surcharge - 25% of meter fare
# - 12am - 6am: time-based surcharge - 50% of meter fare

import math

def get_taxi_fare():

    flag_down = float(input("What's the flag-down fare: $"))
    rate_per_400 = float(input("What's the rate per 400 meters within 9.8km? $"))
    rate_per_350 = float(input("What's the rate per 350 meters beyond 9.8km? $"))
    dist_in_meters = int(input("What's the distance traveled (in meters)? "))
    
    is_peak = input("Is the ride during a peak period? [yes/no] ")
    # CHECKS IF MIDNIGHT ONLY IF NOT PEAK
    if is_peak == "no":
        is_midnight = input("Is the ride between midnight and 6am? [yes/no] ")
    
    is_loc_surcharge = input("Is there any location surcharge? [yes/no] ")
    # CHECKS FOR LOCATION SURCHARGE ONLY IF THERE IS
    if is_loc_surcharge == "yes":
        loc_surcharge = float(input("What's the amount of location surcharge? $"))

    # CONSTANTS
    DIST_THRESHOLD_1 = 1000
    DIST_THRESHOLD_2 = 9800
    total_fare = 0

    # CHECK 1: FIRST 1KM - FLAG-DOWN FARE
    beyond_9800 = max(dist_in_meters - DIST_THRESHOLD_2, 0)
    rem_dist = dist_in_meters - beyond_9800
    upto_9800 = max(rem_dist - DIST_THRESHOLD_1, 0)
    base_dist = rem_dist - upto_9800 # flagdown fare

    # FIRST 1KM
    meter_fare = flag_down
    # 1KM - 9.8KM
    # note: roundup using math.ceil()
    meter_fare += math.ceil(upto_9800/400) * rate_per_400
    # BEYOND 9.8KM
    # note: roundup using math.ceil()
    meter_fare += math.ceil(beyond_9800/350) * rate_per_350
    # ADD TO TOTAL_FARE
    total_fare += meter_fare

    # IF PEAK: +25%
    if is_peak == "yes": time_surcharge = meter_fare * 0.25
    # IF MIDNIGHT: +50%
    elif is_midnight == "yes": time_surcharge = meter_fare * 0.50
    # IF NEITHER PEAK NOR MIDNIGHT
    else: time_surcharge = 0
    # ADD TO TOTAL_FARE
    total_fare += time_surcharge

    if is_loc_surcharge == "yes": total_fare += loc_surcharge
    print(f"The total fare is ${round(total_fare, 2)}")

get_taxi_fare()

# ALL CASES PASSED
# EXPECTED OUTCOME - CASE 1:
# no peak, yes midnight, yes loc surcharge
# What's the flag-down fare: $3.50
# What's the rate per 400 meters within 9.8km? $0.22
# What's the rate per 350 meters beyond 9.8km? $0.22
# What's the distance traveled (in meters)? 11400
# Is the ride during a peak period? [yes/no] no
# Is the ride between midnight and 6am? [yes/no] yes
# Is there any location surcharge? [yes/no] yes
# What's the amount of location surcharge? $3.00
# The total fare is $17.16

# EXPECTED OUTCOME - CASE 2:
# yes peak, no loc surcharge
# What's the flag-down fare: $3.90
# What's the rate per 400 meters within 9.8km? $0.30
# What's the rate per 350 meters beyond 9.8km? $0.30
# What's the distance traveled (in meters)? 8750
# Is the ride during a peak period? [yes/no] yes
# Is there any location surcharge? [yes/no] no
# The total fare is $12.38

# EXPECTED OUTCOME - CASE 3:
# no peak, no surcharge, yes loc surcharge
# What's the flag-down fare: $3.50
# What's the rate per 400 meters within 9.8km? $0.22
# What's the rate per 350 meters beyond 9.8km? $0.22
# What's the distance traveled (in meters)? 11400
# Is the ride during a peak period? [yes/no] no
# Is the ride between midnight and 6am? [yes/no] no
# Is there any location surcharge? [yes/no] yes
# What's the amount of location surcharge? $3.00
# The total fare is $12.44