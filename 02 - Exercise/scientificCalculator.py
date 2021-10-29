#Scientific Calculator Exercise
import os
import datetime as dt
import pytz
import math

os.system('cls')

#Input Data
def calc():
    a  = float(input('Input number    : '))
    op = input('''(type "help" for operator command)
Input operator  : ''')

    #Recalculate prompt
    def repeat():
        repeat = input('\nDo you want to re-calculate? (y/n) : ')
        if repeat =='y':
            os.system('cls')
            calc()
        elif repeat == 'n':
            os.system('cls')
            print('Program has stopped...')
            print('Thank you!')
            print('©whtsvn\n')
        else:
            print('Wrong selection!')
            wait = input("Exiting program...")
            os.system('cls')

    #Processing and Output
    if op == 'help':
        print("+\t Addition")
        print("-\t Subtraction")
        print("*\t Multiplication")
        print("/\t Division\n")
        print("^\t Exponen")
        print("rt\t Root")
        print("%\t Percent")
        print("!\t Factorial")
        print("log\t Logarithm")
        print("ln\t Natural Logarithm\n")
        print("sin\t Sinus")
        print("cos\t Cosinus")
        print("tan\t Tangen\n")
        calc()
    elif op == '+':
        b = float(input('Input number    : '))
        print(23*"=")
        c = a + b
        print(f"{a} + {b}\t\t= {c}")    
    elif op == '-':
        b = float(input('Input number    : '))
        print(23*"=")
        c = a - b
        print(f"{a} - {b}\t\t= {c}")    
    elif op == '*':
        b = float(input('Input number    : '))
        print(23*"=")
        c = a * b
        print(f"{a} x {b}\t\t= {c}")    
    elif op == '/':
        b = float(input('Input number    : '))
        print(23*"=")
        c = a / b
        print(f"{a} : {b}\t\t= {c}")
    elif op == '^':
        b = float(input('Input number    : '))
        print(23*"=")
        c = a ** b
        if b == int('2'):
            print(f"{int(a)}\u00B2\t\t= {int(c)}")
        elif b == int('3'):
            print(f"{int(a)}\u00B3\t\t= {int(c)}")
        else:
            print(f"{int(a)}\u2071\t\t= {int(c)}")
    elif op == 'rt':
        b = float(input('Input number    : '))
        print(23*"=")
        c = a * (1 / b)
        if b == int('2'):
            print(f"\u00B2\u221A{int(a)}\t\t= {int(c)}")
        elif b == int('3'):
            print(f"\u00B3\u221A{int(a)}\t\t= {int(c)}")
        else:
            print(f"\u2071\u221A{int(a)}\t\t= {int(c)}")
    elif op == '%':
        print(23*"=")
        c = a / 100
        print(f"{int(a)} %\t\t= {c}")
    elif op == '!':
        print(23*"=")
        c = 1
        for i in range(1, int(a) + 1):
            c *= i
        print(f"{int(a)}!\t\t: {int(c)}")
    elif op == 'log':
        b = float(input('Input number (i)= '))
        print(23*"=")
        c = math.log(a, b)
        print(f"\u2071log {a}\t\t: {c}")
    elif op == 'ln':
        print(23*"=")
        b = math.log(2.7183, a)
        c = 1 / b
        print(f"ln {a}\t\t= {c}")
    elif op == 'sin':
        print(23*"=")
        c = math.sin(math.radians(a))
        print(f"sin {int(a)}\u00B0\t= {c}")
    elif op == 'cos':
        print(23*"=")
        c = math.cos(math.radians(a))
        print(f"cos {int(a)}\u00B0\t= {c}")
    elif op == 'tan':
        print(23*"=")
        c = math.tan(math.radians(a))
        print(f"tan {int(a)}\u00B0\t= {c}")
    else:
        print(f"There is no '{op}' operator")
        wait = input("Press Enter to continue...")
        repeat()

    repeat()

#Header
gmt = pytz.timezone('Asia/Jakarta')
today = dt.datetime.now(gmt)
title = 'scientific calculator'
print(f"{today:%A, %y-%m-%d (%I:%M:%S %p) %Z %z}")
print(5*"=",title.title(),5*"=")
calc()