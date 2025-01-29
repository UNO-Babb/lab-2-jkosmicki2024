#FutureTime.py
#Name:Jacob K.
#Date:1/29/2025
#Assignment:Lab 1

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currenthour = (now.hour - 6) % 12
  currentminute = now.minute

  print (currenthour, currentminute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours = input("Enter hours: ")
  hours = int(hours)

  minutes = input("Enter minutes: ")
  minutes = int(minutes) 
  futureHour = (currenthour + hours) % 12
  futureminute = (currentminute + minutes) % 60
  strhour = str(futureHour)
  strmin = str(futureminute)
  if futureminute < 10:
    strmin = "0" + strmin
  extrahours = (futureHour // 60) % 12
  futurehour = (extrahours + futureHour)

  print(futureHour)
  print(futureminute)
  #Ask user for minutes

  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
