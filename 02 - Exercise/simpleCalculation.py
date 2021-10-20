#Simple Calculation Exercise
import os

repeat = 'y'
while(True):

    #Celcius Conversion
    def celcius():
        c = float(input('Input temperature value (°C): '))
        print('\nOutput')
        r  = (c*4)/5
        f  = ((c*9)/5)+32
        k  = c+273.15
        ra = (c+273.15)*(9/5)
        print('Reamur     :',r,'°R')
        print('Fahrenheit :',f,'°F')
        print('Kelvin     :',k,'°K')
        print('Rankine    :',ra,'°Ra')

    #Reamur Conversion
    def reamur():
        r = float(input('Input temperature value (°R): '))
        print('\nOutput')
        c  = (r*5)/4
        f  = ((r*9)/4)+32
        k  = c+273.15
        ra = (c+273.15)*(9/5)
        print('Celcius    :',c,'°C')
        print('Fahrenheit :',f,'°F')
        print('Kelvin     :',k,'°K')
        print('Rankine    :',ra,'°Ra')

    #Fahrenheit Conversion
    def fahrenheit():
        f = float(input('Input temperature value (°F): '))
        print('\nOutput')
        c  = (f-32)*(5/9)
        r  = (f-32)*(4/9)
        k  = c+273.15
        ra = (c+273.15)*(9/5)
        print('Celcius    :',c,'°C')
        print('Reamur     :',r,'°R')
        print('Kelvin     :',k,'°K')
        print('Rankine    :',ra,'°Ra')

    #Kelvin Conversion
    def kelvin():
        k = float(input('Input temperature value (°K): '))
        print('\nOutput')
        c  = k-273.15
        r  = (c*4)/5
        f  = ((c*9)/5)+32
        ra = (c+273.15)*(9/5)
        print('Celcius    :',c,'°C')
        print('Reamur     :',r,'°R')
        print('Fahrenheit :',f,'°F')
        print('Rankine    :',ra,'°Ra')

    #Rankine Conversion
    def rankine():
        ra = float(input('Input temperature value (°Ra): '))
        print('\nOutput')
        c  = (ra*(5/9))-273.15
        r  = (c*4)/5
        f  = ((c*9)/5)+32
        k  = c+273.15
        print('Celcius    :',c,'°C')
        print('Reamur     :',r,'°R')
        print('Fahrenheit :',f,'°F')
        print('Kelvin     :',k,'°K')

    #Display Menu
    def menu():
        print('Select the unit to convert : ')
        print("1. Celcius      (Type 'c')")
        print("2. Reamur       (Type 'r')")
        print("3. Fahrenheit   (Type 'f')")
        print("4. Kelvin       (Type 'k')")
        print("5. Rankine      (Type 'ra')")

    #Main Program
    print('Temperature Unit Conversion')
    print('===========================')
    menu()
    select = input("\nYour selection : ")
    print('===========================')

    if select == ('c') or select == ('1'):
        celcius()
    elif select == ('r') or select == ('2'):
        reamur()
    elif select == ('f') or select == ('3'):
        fahrenheit()
    elif select == ('k') or select == ('4'):
        kelvin()
    elif select == ('ra') or select == ('5'):
        rankine()
    else:
        print('The value you entered is incorrect!')

    repeat = input('\nDo you want to re-convert? (y/n) : ')
    if repeat =='y':
        os.system('cls')
        continue
    elif repeat == 'n':
        os.system('cls')
        print('Program has stopped...')
        print('Thank you!')
        print('©whtsvn\n')
        break
    else:
        print('Wrong selection!\n')
        wait = input("Press Enter to continue...")

    os.system('cls')