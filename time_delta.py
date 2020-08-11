#
# Example file for working with timedelta objects 
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# The timedelta is a span of time, not a particular date or time 
# We can use this class for time-based math/calculations 

####################################################################################################################

# Constructing a basic timedelta and print it
# To build a basic timedelta, all we need to do is to create a timedelta class and pass in
# print(timedelta(days=365, hours=5, minutes=1))

# # Printing today's date
# now = datetime.now()
# print("Today is: " + str(now))

# # Printing today's date one year from now 
# print("One year from it will be: " + str(now + timedelta(days=365)))

# # Creating timedelta that uses multiple arguments 
# print("In 2 days and 3 weeks, it will be " + str(now + timedelta(weeks=3, days=2)))

# # Calculating the date 1 week ago, formatting as a string
# t = datetime.now() - timedelta(weeks=1)
# # First we take the date for today by typing datetime.now() then we subtracted timedelta(weeks=1)
# # In other words, we took today's date and subtracted one week from it 
# s = t.strftime("%A %B %d, %Y")
# # Here we are formatting our answer to Day Month (1st-30th), Year
# print("One week ago it was: " + s)
# Finally, we are printing the result out

# How many days until April Fool's Day?
today = date.today()
afd = date(today.year, 4, 1)


if (afd < today):
    print("April Fool's day already went by %d days ago" % ((today - afd).days))   
    afd = afd.replace(year = today.year + 1)
elif (afd > today):
    time_to_afd = afd - today
    print("It's just ", time_to_afd.days, "days until April Fool's Day")

####################################################################################################################

