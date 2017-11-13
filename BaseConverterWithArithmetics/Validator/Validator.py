'''
Created on Nov 13, 2017

@author: Gabriel Em
'''
class Validator:
    def __init__(self):
        pass
    
    def checkInt(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False
    
    def checkValidOption(self, value, maxValue):
        if self.checkInt(value) == False:
            return -1
        elif int(value) < 0 or int(value) > maxValue:
            return -2
        else:
            return 0