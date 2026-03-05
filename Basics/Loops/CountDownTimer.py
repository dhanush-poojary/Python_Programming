import time

MyTime = int(input("Enter the No of seconds: "))

for i in range(MyTime,0,-1):
    seconds = i %60
    minutes = (i//60) %60
    hours = (i//3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")