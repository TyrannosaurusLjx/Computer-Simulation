import random

def systime():
    S = 2
    time = 0
    if S == 2:
        time += rdtime()
        S -= 1
        return systime()
    if S == 1:
        temp = rdtime()
        time += temp
        if temp >= 3:
            S = 1
        else:
            S = 0
        return systime()
    if S == 0:
        print("time is" , time)
        return time

def rdtime():
    return random.randint(1,6)
systime()
