class myclass():
    def method1(self):
        print("This is method 1")

    def method2(self, somestring):
        print("This is method2"+somestring)
class anotherclass():
    def method1(self):
        myclass.method1(self)
        print("this is another class method1" )
    def method2(self,somestring):
        print("this is another class method2")
def main():
    c=myclass()
    c.method1()
    c.method2(" And a string attached")
    c2=anotherclass()
    c2.method1()
    c2.method2("string")
#inheritance

if __name__=="__main__":
    main()
