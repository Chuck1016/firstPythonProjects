import datetime

def Greeting():
    today = datetime.date.today()
    now = datetime.datetime.today()
    date = today.day
    year = today.year
    month = today.month
    monthName = today.strftime("%B")
    weekDay = today.weekday()
    weekDayName = today.strftime("%A")
    fullDate = today.strftime("%B %d, %Y")
    suffix = 0

    if date == 1:
          suffix = 'st'
    elif date == 2:
          suffix = 'nd'
    elif date == 3:
          suffix = 'rd'
    else:
          suffix = 'th'
          
    if 5 <= now.hour < 12:
        daytime = 'Good monring, '
    elif 12 <= now.hour < 17:
        daytime = 'Good afternoon, '
    elif 17 <= now.hour < 21:
        daytime = 'Good evening, '
    else:
        daytime = "Shouldn't you be sleeping? "

    greeting = daytime +"today is " +weekDayName +" the " +str(date) +suffix +" of " +monthName +", " +str(year) +"."
    return greeting
    
##  -----------------------------------------------------------
    
import sys, time

def slowPrint(text, delay=0.025):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print
    
##  From IDLE or Terminal, call the following:
##  import myFunctions as mf
##  new = mf.Greeting()
##  mf.slowPrint(new)
