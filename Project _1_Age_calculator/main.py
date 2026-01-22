import time 
from calendar import isleap

#isleap function is used to determine a year is a leap year or a normal year 
def leap_year_or_not(year):
    if isleap(year):
        return True
    else : 
        return False

#This function is used to assign no of days to a given month 
def month_and_days(month, leap_year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2 and leap_year :
        return 29
    elif month == 2 and (not leap_year) :
        return 28

name = input("Enter your name: ")
age = input("Enter your age :")
localtime = time.localtime(time.time()) # time.time() is used to Returns the current time as the number of seconds since January 1, 1970 (called the Unix epoch)
#this above line of code is used to get current time and date 

year = int(age)
month = year * 12 + localtime.tm_mon 
#what does tm_mon mean 
# Returns an integer from:
# 1 = January
# 12 = December
day = 0


begin_year = int(localtime.tm_year) - year 
end_year = begin_year + year

for y in range(begin_year, end_year):
    if(leap_year_or_not(y)):
        day = day + 366
    else:
       day = day + 365

leap_year = leap_year_or_not(localtime.tm_year)
for m in range(1 , localtime.tm_mon):
    day = day + month_and_days(m, leap_year)

day = day + localtime.tm_mday

print("%s age is %d years or " % (name, year ), end="")
print("%d months or %d days " % (month, day))


    