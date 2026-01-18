'''
Understanding and implementing concurrency using threading
'''
import time
import threading

def func1():
    print("Inside func 1")
    for i in range(3):
        time.sleep(1)
        print("Func 1")

def func2():
    print("Inside func 2")
    for i in range(5):
        time.sleep(0.8)
        print("Func 2")

threading.Thread(target=func1).start()
threading.Thread(target=func2).start()

print("Threads start")

'''
Output obtained:
Inside func 1
Inside func 2
Threads start
Func 2
Func 1
Func 2
Func 1
Func 2
Func 1
Func 2

This is expected as the main python function and these 2 defined functions 
are running on different threads.
'''