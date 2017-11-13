'''
Created on Nov 13, 2017

@author: Gabriel Em
'''

import os
from Validator.Validator import Validator

class UI:
    def __init__(self, controller):
        self._controller = controller
        self._validator = Validator()
    
    # Menus
    
    def mainMenu(self):
        menuOptions = {1:["1.Conversions", self._convertionsMenu],2:["2.Arithmetics", self._arithmeticsMenu]}
        self._runMenu(menuOptions, True)

    def _convertionsMenu(self):
        menuOptions = {1:["1.Direct conversions", self._DirectConversions],2:["2.Conversions using an intermediary base", self._IndirectConversions],3:["3.Quick conversions between bases that are powers of 2", self._QuickConversions]}
        self._runMenu(menuOptions, False)

    def _arithmeticsMenu(self):
        menuOptions = {1:["1.Addition", self._Addition],2:["2.Subtraction", self._Subtraction],3:["3.Multiplication", self._Multiplication],4:["4.Division", self._Division]}
        self._runMenu(menuOptions, False)

    # Menu methods
    
    def _runMenu(self, menuOptions, isMainMenu):
        opt = -1
        while opt != 0:            
            self._printMenu(menuOptions, isMainMenu)
            
            opt = self._readOption(len(menuOptions))
            if opt in menuOptions:
                menuOptions[opt][1]()
                
    def _readOption(self, maxValue):
        opt = -1
        validOption = False
        
        while validOption == False:
            opt = input("\nChoose an option: ")
            validationCode = self._validator.checkValidOption(opt, maxValue)
            
            if validationCode == -1:
                print("The option must be an integer!")
            elif validationCode == -2:
                print("Option " + opt + " is not part of the menu.")
            else:
                validOption = True
    
        return int(opt)
        
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

    # Conversion menu methods
    
    def _DirectConversions(self):
        pass
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