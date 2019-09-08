import os
from os import path
import datetime
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main():
    print(os.name)
    print("Exist:"+str(path.exists("textfile.txt")))
    print("Is a file:"+str(path.isfile("textfile.txt")))
    print("Is a dir:"+str(path.isdir("textfile.txt")))
    print("Item path:"+str(path.realpath("textfile.txt")))
    print("path and name:"+str(path.split((path.realpath("textfile.txt")))))



if __name__=="__main__":
    main()
