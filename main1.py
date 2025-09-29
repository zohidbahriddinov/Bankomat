import os
os.system("cls")
import time

# def sonlar(func):
#     def summa():
#         start = time.time()
#         r = func()
#         end = time.time()
#         print(f'{func.__name__} = {end - start}')
#     return summa


# @sonlar
# def son():
#     s = 0
#     for i in range(1 , 100_000_000):
#         s += 1
   
# son()

def ismi(func):
    def fam():
        start = time.time()
        print("Zohid")
        func()
        print("Baxriddinov")
        end = time.time()
        print(end - start)
    return fam


@ismi
def i_fam():
    print("#####")


i_fam()