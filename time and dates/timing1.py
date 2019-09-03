from datetime import date, time, datetime

def main():
    today= date.today()
    print("Today's date is  ",today) #todays date
    print("Date componenents:",today.day,today.month,today.year)#notice the comma
    print("Today's weekday is :",today.weekday())
    days=["mon","tue","wed","thurs","fri","sat","sun"]
    print("Which is a",days[today.weekday()])
    today=datetime.now()
    print("Current time and date:",today)
    time=datetime.time(datetime.now())
    print("time is :",time)

if __name__=="__main__":
    main()

