def days_till_chrismas(day, month):
    # TODO: For now we assume every month has 30 days
    months = [30 for x in range(12)]
    day_count = 0

    # Add remaining days of the current month
    day_count += months[month] - day

    # Add days from the next month till november (included)
    for i in range(month+1, 11):
        day_count += months[i]

    # Add days in december
    day_count += 24

    return day_count


d = days_till_chrismas(14, 2)

print(d)

'''
Solution works by comparing user input date with relevant christmas of the user input year.
Admittedly stolen from the Python Standard Library. Countdown to event example was reworked and applied
for the case at hand.
'''
__author__ = "5184262: Dominik Ploner"
# Importing the modules necessary for this programme.
import time
from time import mktime
import datetime
from datetime import date  # Importing the modules necessary for this programme.
# User enters a date. This results in an input str(). Needs to be converted.
user_date = input("Please enter the date in the format DDMMYYYY: ")
# Converting input(str) into time.time_struct object.
user_date_parsed = time.strptime(user_date, "%d%m%Y")
# Convert time.time_struct object into datetime.
user_date_parsed_2 = date.fromtimestamp(mktime(user_date_parsed))
# Define christmas variable. Take year from input str().
christmas = date(user_date_parsed.tm_year, 12, 25)
# The loop comparing relevant christmas with user input.
if christmas == user_date_parsed_2:
    print("M E R R Y    C H R I S T M A S!")
# The case in which the user input is after December, 25th. 
elif christmas < user_date_parsed_2:
    christmas = christmas.replace(year=user_date_parsed.tm_year + 1)
days_to_christmas = abs(christmas - user_date_parsed_2)
print(days_to_christmas.days)
