def func1():
    print("this is a Function")

func1()
print (func1())

def func2(arg1,arg2):
    print(arg1," ",arg2)

func2(10,20)
print(func2(10,20))

def cube(x):
    return x*x*x

print(cube(2))

def power(num,x=1):
    result=1
    for i in range(x):
        result=result*num
    return result
print(power(2))
print(power(2,3))
print(power(x=3,num=2)) #argument order does not matter

def multi_add(*args): #multiarguments
    result=0
    for i in args:
        result=result+i
    return result

print(multi_add(2,3,4,5))