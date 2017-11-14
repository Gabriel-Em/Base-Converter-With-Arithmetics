import os

class UI:
    def __init__(self, controller):
        self._controller = controller
    
    # Menus
    
    def mainMenu(self):
        menuOptions = {1:["1.Conversions", self._convertionsMenu], 2:["2.Arithmetics", self._arithmeticsMenu]}
        self._runMenu(menuOptions, True)

    def _convertionsMenu(self):
        menuOptions = {1:["1.Direct conversions", self._DirectConversions], 2:["2.Conversions using an intermediary base", self._IndirectConversions], 3:["3.Quick conversions between bases that are powers of 2", self._QuickConversions]}
        self._runMenu(menuOptions, False)

    def _arithmeticsMenu(self):
        menuOptions = {1:["1.Addition", self._Addition], 2:["2.Subtraction", self._Subtraction], 3:["3.Multiplication", self._Multiplication], 4:["4.Division", self._Division]}
        self._runMenu(menuOptions, False)
    
    def _runMenu(self, menuOptions, isMainMenu):
        opt = -1
        while opt != 0:            
            self._printMenu(menuOptions, isMainMenu)
            
            opt = self._readOption(len(menuOptions))
            if opt in menuOptions:
                menuOptions[opt][1]()
        

    # Conversion menu methods
    
    def _DirectConversions(self):
        sourceBase = self._readBase("\nChoose a base (2 to 16): ")
        strNumber = self._readNumber(sourceBase)
        destinationBase = self._readBase("\nChoose a base (2 to 16) to which the number should be converted: ")
        
        while sourceBase == destinationBase:
            print("The two bases must not be the same!")
            destinationBase = self._readBase("\nChoose a base (2 to 16) to which the number should be converted: ")
        
        convertedNumber = self._controller.convertDirectly(strNumber, sourceBase, destinationBase)
        os.system('CLS')
        self._printTitle()
        print("The number " + strNumber + " converted from base " + str(sourceBase) + " to base " + str(destinationBase) + " is " + str(convertedNumber))
        input("\n\nPress Enter to continue...")
        
    def _IndirectConversions(self):
        pass
    def _QuickConversions(self):
        pass
    
    # Arithmetics menu methods
    
    def _Addition(self):
        pass
    def _Subtraction(self):
        pass
    def _Multiplication(self):
        pass
    def _Division(self):
        pass

    # Reads
    
    def _readOption(self, maxValue):
        validOption = False
        
        while validOption == False:
            opt = input("\nChoose an option: ")
            validationCode = self._controller.checkValidOption(opt, maxValue)
            
            if validationCode == -1:
                print("The option must be an integer!")
            elif validationCode == -2:
                print("Option " + opt + " is not part of the menu.")
            else:
                validOption = True
    
        return int(opt)

    def _readBase(self, message):
        validBase = False
        
        while validBase == False:
            base = input(message)
            validationCode = self._controller.checkValidBase(base)
            
            if validationCode == -1:
                print("The base must be an integer!")
            elif validationCode == -2:
                print("The base must be >= 2 and <= 16.")
            else:
                validBase = True
    
        return int(base)

    def _readNumber(self, base):
        validNumber = False
        
        while validNumber == False:
            number = input("\nChoose a number in base " + str(base) + ": ")
            validationCode = self._controller.checkValidNumber(number, base)
            
            if validationCode == -1:
                print("The number can't be zero or null.")
            elif validationCode == -2:
                print("That number is not written in base " + str(base) + "!")
            else:
                validNumber = True
    
        return number
    
    # Prints
    
    def _printMenu(self, menuOptions, isMainMenu):
        os.system('CLS')        
        self._printTitle()
        print("Menu:\n")
        for key in menuOptions:
            print(menuOptions[key][0])
        
        if isMainMenu:
            print("0.Exit")
        else:
            print("0.Back to the previous menu")
        
    def _printTitle(self):
        title = '''\

                                      >>> Base converter with arithmetics <<<
'''
        print(title)
    
