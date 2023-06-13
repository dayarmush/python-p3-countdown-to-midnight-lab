import time

def countdown(x):
    while x >= 1:
        print(f'{x} SECOND(S)!')
        x -= 1
        if x == 0:
            print('HAPPY NEW YEAR!')


def countdown_with_sleep(x):
    while x >= 1:
        print(f'{x} SECOND(S)!')
        time.sleep(1)
        x -= 1
        if x == 0:
            print('HAPPY NEW YEAR!')       
