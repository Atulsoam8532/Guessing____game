#Athematic +, -, /, *, //, **, %

num1 = int(input("enter your first number"))
opration = input("+,-,*,/,//,**,%")
num2 = int(input("enter your second number"))

if opration == '+':
    print("The sum of these numbers is ", num1+num2)
elif opration == '-':
    print("The subtraction of these numbers is ",  num1-num2)
elif opration == '*':
    print("The multiplication of these number is ", num1*num2)
elif opration == '//':
    print("The divide of these numbers is ", num1//num2)
elif opration == '**':
    print("The square of these numbers is ", num1**num2)
elif opration == '%':
    print("The module of these numbers is ", num1%num2)
else:
    print("invalid number")
#Assignment =, +=, -=, //=, /=, *=, **=
from builtins import bool
#for +=
x = int(input("enter a number:"))
x += 2
print(x)
#for -=
y = int(input("enter a number: "))
y -= 1
print(y)
#for//=
z = int(input("enter a number: "))
z //= 2
print(z)
#for/=
a = int(input("enter a number: "))
a /= 2
print(a)
#for*=
b = int(input("enter a number: "))
b *= 2
print(b)
#for**=
c = int(input("enter a number: "))
c **= 2
print(c)
#Comparison ==, >, <, >=, <=

x = int(input("enter your first number: "))
y = int(input("enter your second numbe: "))

#for ==
print("x==y is", x==y)
#for>
print("x>y is", x>y)
#for<
print("x<y is", x<y)
#for>=
print("x>=y is", x>=y)
#for<=
print("x<=y is", x<=y)
#Logical And, or, not

x = int(input("enter a number: "))
y = int(input("enter a number: "))
z = int(input("enter a number: "))

#for And
print(x==y and y==z)
#for OR
print(x==y or y>z)
#for not
print(not x==y )
#Identify operator

a = int(input("enter a number: "))
b = int(input("enter a number"))

#for checking memory location
print(id(a))
print(id(b))
#for is
print(a is b)
#for is  not
print(a is not b)
#Membership operator'IN' and ' NOT IN'
a = input("enter something")
b = input("enter something")

#for in
print(a in b)
#for not in
print(a not in b)



