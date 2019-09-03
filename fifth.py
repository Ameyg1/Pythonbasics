def main():
    x=0
    while(x<5):
       print(x)
       x=x+1
    for x in range(5,10):
        print(x)
    days=["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"]
    for d in days: #no counter needed
        print(d)
        #break
        for x in range(10,20):
            if(x==15) :break
            print(x)
            #continuestatementfor (oddnumber only)
        for x in range(10,20):
            if(x%2==0):continue
            print(x)
            #for index use enumerate function
        days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
        for i,d in enumerate(days):
            print(i, d)

if __name__=="__main__":
    main()