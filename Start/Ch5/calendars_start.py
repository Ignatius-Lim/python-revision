#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
# thestr = c.formatmonth(2026,4,0,0)
# print(thestr)

# create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# thestr = hc.formatmonth(2026,4)
# print(thestr)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# For example, April 2026 starts with Wed. So the first Sun to Wed are 0's.
# for i in c.itermonthdays(2026, 4):
#   print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
#   print(name)

# for day in calendar.day_name:
#   print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on:")
for m in range(1, 13):
  cal = calendar.monthcalendar(2026, m)

  # The first Friday of a month has to be within the first or second week of a month.
  # If the 1st week starts from Saturday, for sure the first Friday falls on the 2nd week
  weekone = cal[0] # First week
  weektwo = cal[1] # Second week

  if weekone[calendar.FRIDAY] != 0:
    meetday = weekone[calendar.FRIDAY]
  else:
    meetday = weektwo[calendar.FRIDAY]

  print(f"{calendar.month_name[m]}: {meetday}")