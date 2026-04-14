#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
today = date.today()
# print(f"Today's date is {today}")


# print out the date's individual components
# print(f"Day: {today.day}\nMonth: {today.month}\nYear: {today.year}")


# retrieve today's weekday (0=Monday, 6=Sunday)
print(f"Weekday: {today.weekday()}")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print("Today is", days[today.weekday()])


## DATETIME OBJECTS
# Get today's date from the datetime class
today = datetime.now()
print(f"The current date and time is {today}")


# Get the current time
t = datetime.time(datetime.now())
print(f"The current time is {t}")
