# import os
# os.system("cls")
# import time

# # def sonlar(func):
# #     def summa():
# #         start = time.time()
# #         r = func()
# #         end = time.time()
# #         print(f'{func.__name__} = {end - start}')
# #     return summa


# # @sonlar
# # def son():
# #     s = 0
# #     for i in range(1 , 100_000_000):
# #         s += 1
   
# # son()

# # def ismi(func):
# #     def fam():
# #         start = time.time()
# #         print("Zohid")
# #         func()
# #         print("Baxriddinov")
# #         end = time.time()
# #         print(end - start)
# #     return fam


# # @ismi
# # def i_fam():
# #     print("#####")

# # i_fam()

# # # decorator - funksiyani argument sifatida olib, uning o’zgartirilgan
# # # nusxasini qaytaruvchi funksiya.  Decorator bevosita funksiyani
# # # o’zgartirmasdan, undan oldin va keyin ishlaydigan kodlar qo’shish
# # # imkonini beradi.


# def my_decorator(func):
#     def wrapper():
#         print("Funktsiyadan oldin ishlayapti")
#         func()
#         print("Funktsiyadan keyin ishlayapti")

#     return wrapper


# @my_decorator
# def say_hello():
#     print("Salom, dunyo!")


# # say_hello()


# # def repeat(n):
# #     def decorator(func):
# #         def wrapper(*args, **kwargs):
# #             for _ in range(n):
# #                 func(*args, **kwargs)
# #
# #         return wrapper
# #
# #     return decorator
# #
# #
# # @repeat(2)
# # def greet(name):
# #     print(f"Salom, {name}!")


# # greet("Ali")


# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Funksiya chaqirildi: {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Natija: {result}")
  
#     return wrapper

# # @log_decorator
# # def add(a, b):
# #     return a + b

# # add(3, 5)

# def count_dec(func):
#     def wrapper():
#         start = time.time()
#         result = func()
#         end = time.time()

#         print(f'{func.__name__} ning ishlash vaqti {end-start}')
#     return wrapper

# @count_dec
# def counter():
#     count = 0
#     for i in range(1, 100_000_000):
#         count += 1

# counter()


