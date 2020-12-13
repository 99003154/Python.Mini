#!/usr/bin/python
# -*- coding: utf-8 -*-
# Advanced Mathematical Functions Calculator
# Banking Operations
# This function finds the Annual Percentage Yield
# r is stated annual interest rate
# n is number of times compounded
# This function finds the loss


def loss(s, c):
    return c - s


def ctof(c):
    return c * 9 / 5 + 32


# This function converts temperature from celsius to kelvin

def ctok(c):
    return c + 273.15


# This function converts temperature from fahrenheit to celsius

def ftoc(f):
    return (f - 32) * 5 / 9


# This function converts temperature from fahrenheit to kelvin

def ftok(f):
    return (f - 32) * 5 / 9 + 273.15


# This function converts temperature from kelvin to celsius

def ktoc(k):
    return k - 273.15


# This function converts temperature from kelvin to fahrenheit

def ktof(k):
    return k - 273.15


# Operations related to measurements
# This function finds area of circle
# r is radius of the circle

def area_circle(r):
    return 3.147 * a * a


# This function finds area of square
# x is the one of the side of the square

def area_square(x):
    return x * x


# This function finds perimeter of square
# a is side of the square

def peri_square(a):
    return 4 * a


# This function finds perimeter of circle
# r is radius of the circle

def peri_circle(r):
    return 2 * 3.147 * r


# This function finds area of triangle
# h is height of the triangle
# b is base of the triangle

def area_triangle(h, b):
    return h * b / 2


# This function finds area of rectangle
# a is smaller side of rectangle
# b is larger side of rectangle

def area_rectangle(a, b):
    return a * b


# This function finds perimeter of rectangle
# l is length of the rectangle
# w is width of the rectangle

def peri_rectangle(l, w):
    return 2 * (l + w)


# This function finds perimeter of triangle
# a is first side of the triangle
# b is second side of the triangle
# c is third side of the triangle

def peri_triangle(a, b, c):
    return a + b + c


print ('Select operation:')
print ('4.loss')
print ('7.ctof')
print ('8.ctok')
print ('9.ftoc')
print ('10.ftok')
print ('11.ktoc')
print ('12.ktoc')
print ('13.area_circle')
print ('14.area_square')
print ('15.peri_square')
print ('16.peri_circle')
print ('17.area_triangle')
print ('18.area_rectangle')
print ('19.peri_triangle')
print ('20.peri_rectangle')
while True:

    # Take input from the user

    choice = input('Enter choice: ')

    # Check if choice is one of the four options

    if choice in (
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16',
    ):
        num1 = float(input('Enter first number: '))
        if choice == '7':
            print (ctof(num1))
        elif choice == '8':
            print (ctok(num1))
        elif choice == '9':
            print (ftoc(num1))
        elif choice == '10':
            print (ftok(num1))
        elif choice == '11':
            print (ktoc(num1))
        elif choice == '12':
            print (ktof(num1))
        elif choice == '13':
            print (area_circle(num1))
        elif choice == '14':
            print (area_square(num1))
        elif choice == '15':
            print (peri_square(num1))
        elif choice == '16':
            print (peri_circle(num1))
        break
    elif choice in (
        '4',
        '17',
        '18',
        '20',
         ):
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        if choice == '4':
            print (loss(num1, num2))
        elif choice == '17':
            print (area_triangle(num1, num2))
        elif choice == '18':
            print (area_rectangle(num1, num2))
        elif choice == '20':
            print (peri_rectangle(num1, num2))
        break
    elif choice in ('19'):
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        num3 = float(input('Enter third number: '))
        if choice == '19':
            print (peri_triangle(num1, num2, num3))
        break
    else:
        print ('Invalid Input')
