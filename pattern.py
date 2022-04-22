from ast import Num
from tkinter import E


n=int(input("Enter the value of n:"))
for i in range(0,n):
    for j in range(0,n-i+1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()

n=int(input("Enter the number: "))
space=n-1
num=1
for i in range(0,n):
    for j in range(0,space):
        print(end=" ")
    space-=1
    for j in range(0,num):
        print(i+1,end=" ")
    num+=2
    print()

