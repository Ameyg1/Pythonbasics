import calendar
c=calendar.TextCalendar(calendar.SUNDAY)
st=c.formatmonth(2019,1,0,0)
print(st)
#html calendar
hc=calendar.HTMLCalendar(calendar.SUNDAY)
st=hc.formatmonth(2019,1)
print(st)
for i in c.itermonthdays(2019,8):
    print(i)
for months in calendar.month_name:
    print(months)
for days in calendar.day_name:
    print(days)
print("team meeting will be on: ")
for m in range(1,13):
    cal=calendar.monthcalendar(2019,m)
    weekone=cal[0]
    weektwo=cal[1]
    if weekone[calendar.FRIDAY]!=0:
        meetday=weekone[calendar.FRIDAY]
    else:
        meetday=weektwo[calendar.FRIDAY]
    print("%10s %2d" %(calendar.month_name[m],meetday))