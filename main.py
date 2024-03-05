excess3Dict = {-3:'000', -2:'001', -1:'010', 0:'011',  1:'100', 2:'101', 3:'110', 4:'111'}


def newNum(firstRun):
    global decNum
    #first run, don't ask if they want a new number, just prompt for a number
    if firstRun == False:
        try:
            newNum = input("Would you like to use a new number? (y/n)\n")
        except(ValueError, TypeError):
            print("Please enter y or n")
            newNum(True)
        else:
            print()
    else:
        newNum = 'y'
    
    #if want new number, exception for input
    if newNum == 'y' or newNum =='Y':
        try:
            decNum = float(input("Please input a decimal number:\t"))
        except(ValueError):
            print("Please input a valid decimal or integer value. Try Again!\n\n")
            newNum(False)
        else:
            if decNum > -8 and decNum <= 15 and decNum != 0:
                toBinary(abs(decNum))
                normalizeBin(decNum)
                menu(decNum)
            else:
                print("Please input a number between -8 and 15, and is not 0 for a 4-bit binary.")
                newNum(False)
    else:
        menu(decNum)

def menu(decNum):
    try:
        selection = int(input("\nPlease select an option:\n1- Convert the inputted decimal to binary\n2- Normalize the inputted binary number\n3- Convert the Inputted Exponent Number to it's corresponding number in excess-3\n4- Input a binary to receive its sign, significand, and exponent\n5- Exit\nSelection:  "))
    except(ValueError):
        print("That is not an accepted value type, please try again!\n\n")
        newNum(False)
    else:
        print()
        if selection == 1:
            toBinaryString(decNum)
            newNum(False)
        elif selection == 2:
            toStringNormalizeBin(decNum)
            newNum(False)
        elif selection == 3:
            toExcessThree()
            newNum(False)
        elif selection == 4:
            bigThree(decNum)
            newNum(False)
        elif selection == 5:
            exitChar = input("Are you sure you'd like to exit? y/n\n")
            if (exitChar == 'y' or exitChar == 'Y'):
                print("Okay, thank you!")
                exit()
            else:
                newNum(False)

# will run with every decimal input.
def toBinary(decimal):
    global fractionalBin, wholeBin
    fractionalBin = ""
    wholeBin = ""
    precision = 3
    leftBin = int(decimal)
    rightBin = decimal - float(leftBin)

    while (leftBin):
        holder = leftBin % 2
        #append hold binary value to the whole number
        wholeBin += str(holder)
        #truncates after division
        leftBin //= 2    

    #for fractional binary with precision of 3 digits
    while (precision):
        rightBin *= 2.0
        fractionBit = int(rightBin)
        if(fractionBit == 1):
            rightBin -= fractionBit
            fractionalBin += '1'
        else:
            fractionalBin += '0'
        precision -= 1

    #check if input number is integer, then no fractional bit
    if fractionalBin == "":
        fractionalBin +="0"
    if wholeBin == '':
        wholeBin += "0"



def toBinaryString(decNum):
    if decNum > 0 :
        print("Your decimal as a binary number: ", wholeBin + '.' + fractionalBin + "\n\n")
    else:
        print("Your decimal as a binary number: -" + wholeBin + '.' + fractionalBin + "\n\n")

def normalizeBin(decimal):
    global exponent, normalBin, fractNormalBin
    if decimal > 1 or decimal < -1:
        exponent = len(wholeBin)-1
        remainDigit = wholeBin[1:len(wholeBin)]
        fractNormalBin = remainDigit + fractionalBin
    elif (decimal < 1 and decimal > 0) or (decimal > -1 and decimal < 0):
        isSig = False
        exponent = 0
        fractNormalBin = fractionalBin
        while not isSig:
            if fractNormalBin[0] == '0':
                fractNormalBin = fractionalBin[1:len(fractionalBin)]
                exponent -= 1
            else:
                isSig = True
                fractNormalBin = fractionalBin[1:len(fractionalBin)]
                exponent -= 1
        while len(fractNormalBin) <=2:
            fractNormalBin+='0'
    else:
        print("Cannot normalize 0! Try again!")
        newNum(False)


def toStringNormalizeBin(decimal):
    if decimal > 1:
        print('Normalized Binary: 1.' + fractNormalBin + "*2^" + str(exponent) + '\n')
    elif decimal < 1 and decimal > 0:
        print('Normalized Binary: 1.' + fractNormalBin + "*2^" + str(exponent) + '\n')
    elif decimal > -1 and decimal < 0:
        print('Normalized Binary: -1.' + fractNormalBin + "*2^" + str(exponent) + '\n')
    elif decimal < -1:
        print('Normalized Binary: -1.' + fractNormalBin + "*2^" + str(exponent) + "\n")
    


def toExcessThree():
    excess3Exponent = excess3Dict[exponent]
    print("Exponent in excess 3: " + excess3Exponent)


def bigThree(decimal):
    excess3Exponent = excess3Dict[exponent]
    if decimal < 0:
        sign = '0'
    else:
        sign = '1'
    toBinaryString(decimal)
    print("Sign | Exponent | Significand\n" + sign + " | " + excess3Exponent + " | " + fractNormalBin + "\n")


newNum(True)