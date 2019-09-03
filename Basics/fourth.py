def main():
    x,y=100,1000
    if(x<y):
        st="x is less than y"
    elif(x>y):
        st="x is greater than y"
    else:
        st="x is equal to y"
    print(st)
    st="x is less than y" if(x<y) else"x is greater than or equal to y" #similar to ternary operator in java
    print(st)


if __name__ == "__main__":
    main()