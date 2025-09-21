import threading
import time
import random

buffer = []

def produtor():
    for i in range(10):
        nums = random.randint(1,100)
        buffer.append(nums)
        print(f"{buffer}")

def consumidor():
    cont = len(buffer) -1
    for i in range(len(buffer)):
        buffer.pop(cont)
        print(f"{buffer}")
        cont -= 1



if __name__ == "__main__":

    produtor()
    consumidor()
