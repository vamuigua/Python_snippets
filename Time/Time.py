#Modules imported
import time
import calendar

#To get the how many seconds passed since 12.00am, Jan 1, 1970
ticks = time.time()
print "Number of ticks since 12.00am, Jan 1, 1970 :",ticks

#To get the current local time
localtime = time.localtime(time.time())
print "Local current time :",localtime

#Get current local time in Readable Format
localtime = time.asctime(time.localtime(time.time()))
print "Local current time :",localtime

#Sleep() method suspends execution of the next code for the given number of seconds
#Suspends the next code for 2 seconds
time.sleep(2)

#Printing a calender for a given month for our example its for August 2016
cal = calendar.month(2016,8)

#Function to show year is a leap year
leapyr = calendar.isleap(2016)

#Function to show the day on the week starts from 0(Monday) to 6(Sunday)
week_day = calendar.weekday(2016,8,9)

#Prints the calender
print "Here is the calender:"
print cal

#Prints True if its a Leap year
print leapyr

#Prints the day_of_the_week
print week_day
