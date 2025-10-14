# flag_down: How much for first 1km (or part thereof)
# rate_400: How much (in $) per 400 m, or part thereof, between 1 km and 9.8 km
# rate_350: How much (in $) per 350 m, or part thereof, beyond 9.8 km
# dist_total: Total distance travelled (in m)
# is_peak: Whether ride is during peak period
def taxi_fare(flag_down, rate_400, rate_350, dist_total, is_peak, is_dawn, is_location, location_surcharge):

    # Calculate meter fare
    meter = meter_fare(flag_down, rate_400, rate_350, dist_total)
    
    # Calculate surchages
    surcharge = surcharge_fare(is_peak, is_dawn)
    
    # Calculate final result
    total_fare = meter * (1 + surcharge)
    if is_location:
        total_fare = total_fare + location_surcharge
    
    return total_fare


def meter_fare(flag_down, rate_400, rate_350, dist_total):

    # Fixed cost (flag down rate) for first 1000m
    FLAG_DOWN_DIST = 1000;
    
    # Boundary between paying per 350m and paying 400m
    DIST_BOUNDARY = 9800;

    # We pay for every 400m (or part thereof) between 1km and 9.8km
    DIST_UNIT_1 = 400;

    # We pay for every 350m (or part thereof) beyond 9.8km
    DIST_UNIT_2 = 350;

    # This allows us to use mathematical functions
    import math
    
    # If distance less than 1km
    if dist_total < FLAG_DOWN_DIST:
        return flag_down
        
    # If distance less than 9.8km
    elif dist_total < DIST_BOUNDARY:
    
        # How far travelled beyond 1km?
        extra_dist = dist_total - FLAG_DOWN_DIST
        
        # Determine how many extra distance units travelled (ignoring flag down distance) or part thereof
        extra_dist_units = math.ceil(extra_dist / DIST_UNIT_1)
            
        # Pay for each 400m over 1km (or part thereof), plus flag down fare
        return flag_down + extra_dist_units * rate_400
        
    # Else, distance 9.8km or more
    else:
    
        # How far travelled beyond 9.8km?
        extra_dist = dist_total - DIST_BOUNDARY
        
        # Determine how many extra distance units travelled (ignoring flag down distance) or part thereof
        extra_dist_units = math.ceil(extra_dist / DIST_UNIT_2)
        
        # Determine how much to pay for distance between 1km and 9.8 km
        middle_cost = (DIST_BOUNDARY - FLAG_DOWN_DIST) / DIST_UNIT_1 * rate_400
            
        # Pay for each 350m over 9.8km (or part thereof), plus flag down fare,
        # plus each 400m between 1km and 9.8 km
        return flag_down + middle_cost + extra_dist_units * rate_350


# Returns percentage surcharge (e.g. 0.5 means 50% surcharge)
def surcharge_fare(is_peak, is_dawn):

    if is_peak:
        return 0.25
    elif is_dawn:
        return 0.5
    else:
        return 0;


# Returns True or False depending on whether given string is "yes" or "no"
def yes_or_no_to_boolean(s):
    if s == "yes":
        return True
    elif s == "no":
        return False
    else:
        return False;
    
    
def test():

#    fare = taxi_fare(flag_down, rate_400, rate_350, dist_total, is_peak, is_dawn, is_location, location_surcharge)
    fare = taxi_fare(3.9, 0.3, 0.3, 8750, True, False, False, 0)
    fare = round(fare, 2)
    print("The total fare is $" + str(fare))
        
        
# Prompt user for decimal number
flag_down = float(input("What's the flag-down fare: $"))

# Prompt user for decimal number
rate_400 = float(input("What's the rate per 400 meters within 9.8km? $"))

# Prompt user for decimal number
rate_350 = float(input("What's the rate per 400 meters beyond 9.8km? $"))

# Prompt user for decimal number
dist_total = float(input("What's the distance traveled (in meters)? "))

# Prompt user for string
is_peak = yes_or_no_to_boolean(input("Is the ride during a peak period? [yes/no] "))

# If not during peak hour, prompt user for string
is_dawn = False
if not is_peak:
    is_dawn = yes_or_no_to_boolean(input("Is the ride between midnight and 6am? [yes/no] "))

# Prompt user for string
is_location = yes_or_no_to_boolean(input("Is there any location surcharge? [yes/no] "))

# If there is a location surcharge, prompt user for decimal number
location_surcharge = 0
if is_location:
    location_surcharge = float(input("What's the amount for location surcharge? $"))

# Use above function to calculate final taxi fare, rounded to 2 decimal places
fare = taxi_fare(flag_down, rate_400, rate_350, dist_total, is_peak, is_dawn, is_location, location_surcharge)
fare = round(fare, 2)
print("The total fare is $" + str(fare))