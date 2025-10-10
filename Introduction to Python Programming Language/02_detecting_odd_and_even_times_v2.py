import datetime
import time
import random

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29,
        31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range(10):
        this_moment = datetime.datetime.today().minute
        if this_moment in odds:
            print("Odd minute")
        else:
            print("Even minute")
            
        wait_time = random.randint(1, 9)
        time.sleep(wait_time)
