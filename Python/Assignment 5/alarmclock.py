import datetime

alarmHour = int(input("Enter hour: "))
alarmMinute = int(input("Enter minute: "))
amPm = input("am or pm: ")

if amPm == "pm":
    alarmHour = alarmHour + 12

while True:
    if alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute:
        print("Wake UP....!!!!")
        break
    
        
