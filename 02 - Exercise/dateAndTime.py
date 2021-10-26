#Date and Time Exercise
import os
import datetime as dt
import pytz

os.system('cls')

#Header
today = dt.datetime.now()
gmt = pytz.timezone('Asia/Jakarta')
timezone = dt.datetime.now(gmt)
title = 'how old are you?'
print(f"{today:%A, %y-%m-%d (%I:%M:%S %p)} {timezone:%Z %z}")
print(5*"=",title.title(),5*"=")

#Input Data
print("Input your place and date of birth")
name  = str(input('Your name : '))
place = str(input('Place     : '))
date  = int(input('Date      : '))
month = int(input('Month     : '))
year  = int(input('Year      : '))
print(28*"=")

#Greetings
def greetings():
    print(f"Good {period_greetings} {name}")
period = (((dt.datetime.now().hour % 24) + 4) // 4)
if period == 1:
    period = str(((dt.datetime.now().hour % 24) + 4) // 4)
    period_greetings = period.replace('1','Late Night')
    greetings()
elif period == 2:
    period = str(((dt.datetime.now().hour % 24) + 4) // 4)
    period_greetings = period.replace('2','Early Morning')
    greetings()
elif period == 3:
    period = str(((dt.datetime.now().hour % 24) + 4) // 4)
    period_greetings = period.replace('3','Morning')
    greetings()
elif period == 4:
    period = str(((dt.datetime.now().hour % 24) + 4) // 4)
    period_greetings = period.replace('4','Afternoon')
    greetings()
elif period == 5:
    period = str(((dt.datetime.now().hour % 24) + 4) // 4)
    period_greetings = period.replace('5','Evening')
    greetings()
else:
    period = str(((dt.datetime.now().hour % 24) + 4) // 4)
    period_greetings = period.replace('6','Night')
    greetings()

#Calculation Process
birth_date = dt.datetime(year,month,date)
age = today - birth_date
age_year = age.days // 365
age_month = (age.days % 365) // 30
age_days = (age.days % 365) % 30

#Output
print(f"You was born in {place} on {birth_date:%B %d, %Y}.")
print(f"You are {age_year} years {age_month} months {age_days} days old. ")

#End of Program
wait = input("\nPress Enter to continue...")
os.system('cls')
print("Program has stopped...")
print("Thank you!")
print("©whtsvn\n")
