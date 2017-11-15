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

    def checkValidBase(self, value):
        if self.checkInt(value) == False:
            return -1
        elif int(value) < 2 or int(value) > 16:
            return -2
        else:
            return 0
    
    def checkValidNumber(self, number, base):
        baseDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        
        while number != "" and number[0] == ' ':
            number = number[1:]
        
        if number == "":
            return -1
            
        for digit in number:
            if digit not in baseDigits:
                return -2
            elif baseDigits.index(digit) >= base:
                return -2
        return 0