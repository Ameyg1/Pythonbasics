def main():
    #f=open("textfile.txt","w+") #opencreate newfile
    #f=open("textfile.txt","a") #append
    f=open("textfile.txt","r")
      for i in range(10):
         f.write("This is line"+str(i)+"\r\n")
     if f.mode=="r":
          contents=f.read()
          print(contents)
    fl=f.readlines()
    for x in fl:
        print(x)
    f.close()

if __name__=="__main__":
    main()