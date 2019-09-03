
from datetime import datetime

def main():
    now=datetime.now()
    #date formatting
    #year=%y
    print(now.strftime("the current year is: %Y"))#regular string is working in strftime
    print(now.strftime("%a,%d,%B,%y" ))
    #%a=abbr day,%d=date,%B=full month,%y=abbr year %A weekday
    #locale data
    print(now.strftime("Locale date and time:%c"))
    print(now.strftime("Locale date:%x"))
    print(now.strftime("Locale time:%X"))
    #timeformatting
    #%I=12 hour %H=24 hour %M=minute %S=seconds %p=am/pm locale
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("Current time: %H:%M"))

if __name__=="__main__":
    main()