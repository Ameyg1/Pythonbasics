from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta
#span of time time based maths
def main():
    print(timedelta(days=365,hours=5,minutes=1))
    now=datetime.now()
    print("today is",now)
    print("one year later:",now+timedelta(days=365))
    print("In two days and three weeks it will be:",now+timedelta(weeks=3,days=2))
    t= now-timedelta(weeks=1)
    print("One week ago",t.strftime("%A %d %B,%Y"))
    today=date.today()
    afd=date(today.year,month=4,day=1)
    if afd<today:
        print("April fools day went away %d ago" %((today-afd).days))
        afd=afd.replace(year=today.year+1)
    timetoafd=afd-today
    print("time to afd:",timetoafd.days)



if __name__=="__main__":
    main()

