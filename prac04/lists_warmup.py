""""
numbers[0]   =3
numbers[-1]  =2
numbers[3]   =1
numbers[:-1] = [3, 1, 4, 1, 5, 9]
numbers[3:4] =[1]
5 in numbers = True
7 in numbers = False
"3" in numbers = False
numbers + [6, 5, 3] =[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

numbers = ["ten", 1, 4, 1, 5, 9, 1]

num1=numbers[2:]
print(num1)
num2=9 in numbers
print(num2)
