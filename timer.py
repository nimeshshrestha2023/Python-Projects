# Programming in python to build as basic timer app

import time

mytime = int(input("Enter the time in second ! "))

for x in range(mytime,0,-1):
    second = x % 60
    minute = int(x / 60) % 60
    hour = int(x / 3600)
    print(f"{hour:02}:{minute:02}: {second:02}")
    time.sleep(1)

print("TIME'S UPPPPPPPP !")