#Comparison and Logic Exercise
import os

repeat = 'y'
while(True):

    #Display Menu
    def menu():
        print("Select logic gates : ")
        print("1. AND")
        print("2. OR")
        print("3. XOR")
        print("4. XNOR")

    #Main Program
    os.system('cls')
    print("Comparison and Logic")
    print("====================")
    menu()
    select = input('\nYour selection : ')
    print("====================")

    #AND Logic
    def andLogic():
        inputUser = int(input('Input a number between 3 and 10: '))
        print("====================")
        lessThan = (inputUser <= 3)
        moreThan = (inputUser >= 10)
        correctNumber = lessThan or moreThan
        print('Number ',inputUser,' is ',correctNumber)
        print("====================")

    def orLogic():
        inputUser = int(input('Input a number less than 3 or more than 10:'))
        print("====================")
        moreThan = (inputUser >= 3)
        lessThan = (inputUser <= 10)
        correctNumber = lessThan and moreThan
        print('Number ',inputUser,' is ',correctNumber)
        print("====================")

    def xorLogic():
        print('Input a number between 3 and 10: ')
        inputUserAnd = int(input('First number: '))
        print('\nInput a number less than 3 or more than 10:')
        inputUserOr = int(input('Second number: '))
        print("====================")
        lessThanAnd = (inputUserAnd <= 10)
        moreThanAnd = (inputUserAnd >= 3)
        correctNumberAnd = lessThanAnd and moreThanAnd
        lessThanOr = (inputUserOr <= 3)
        moreThanOr = (inputUserOr >= 10)
        correctNumberOr = lessThanOr or moreThanOr
        correctNumber = correctNumberAnd ^ correctNumberOr
        print('The first number ',inputUserAnd,' is ',correctNumberAnd)
        print('The second number ',inputUserOr,' is ',correctNumberOr,'\n')
        print(inputUserAnd,' XOR ',inputUserOr,' is ',correctNumber)
        print("====================")

    def xnorLogic():
        print('Input a number between 3 and 10: ')
        inputUserAnd = int(input('First number: '))
        print('\nInput a number less than 3 or more than 10:')
        inputUserOr = int(input('Second number: '))
        print("====================")
        lessThanAnd = (inputUserAnd <= 10)
        moreThanAnd = (inputUserAnd >= 3)
        correctNumberAnd = lessThanAnd and moreThanAnd
        lessThanOr = (inputUserOr <= 3)
        moreThanOr = (inputUserOr >= 10)
        correctNumberOr = lessThanOr or moreThanOr
        correctNumber = correctNumberAnd ^ correctNumberOr
        print('The first number ',inputUserAnd,' is ',correctNumberAnd)
        print('The second number ',inputUserOr,' is ',correctNumberOr,'\n')
        print(inputUserAnd,' XNOR ',inputUserOr,' is ',not(correctNumber))
        print("====================")

    if select == ('1') or select == ('AND'):
        andLogic()
    elif select == ('2') or select == ('OR'):
        orLogic()
    elif select == ('3') or select == ('XOR'):
        xorLogic()
    elif select == ('4') or select == ('XNOR'):
        xnorLogic()
    else:
        print('The value you entered is incorrect!')

    repeat = input('\nDo you want to re-convert? (y/n) : ')
    if repeat =='y':
        os.system('cls')
        continue
    elif repeat == 'n':
        os.system('cls')
        print("Program has stopped...")
        print("Thank you!")
        print("©whtsvn\n")
        break
    else:
        print('Wrong selection!\n')
        wait = input("Press Enter to continue...")