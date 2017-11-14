from Model.Number import Number
from Validator.Validator import Validator

class Controller:
    def __init__(self):
        self._validator = Validator()
    
    def convertDirectly(self, strNumber, sourceBase, destinationBase):
        number = Number(strNumber, sourceBase)
        
        if sourceBase < destinationBase:
            return self._conversionBySubstitution(number, destinationBase)
        else:
            return self._conversionByRepeatedDivision(number, destinationBase)
    
    # Conversion methods
    
    def _conversionBySubstitution(self, number, destinationBase):
        power = 0
        index = len(number) - 1
        listOfTerms = []
        
        while index >= 0:
            term = number[index] * (number.getBase() ** power)
            remainders = []
            while term != 0:
                remainders.insert(0, term % destinationBase)
                term = term // destinationBase
            
            if len(remainders) != 0:
                listOfTerms.append(Number(self._listIntToBaseString(remainders), destinationBase))
            index -= 1
            power += 1
        
        if len(listOfTerms) == 0:
            return Number("0", destinationBase)
        elif len(listOfTerms) == 1:
            return listOfTerms[0]
        else:
            sumOfTerms = self._addition(listOfTerms[0], listOfTerms[1], destinationBase)
            for i in range(2, len(listOfTerms)):
                sumOfTerms = self._addition(sumOfTerms, listOfTerms[i] ,destinationBase)
            return sumOfTerms
        
    
    def _conversionByRepeatedDivision(self, number, destinationBase):
        pass
    
    # Arithmetic operations
    
    def _addition(self, term1, term2, base):
        if len(term1) < len(term2):
            term1.lengthen(len(term2))
        elif len(term1) > len(term2):
            term2.lengthen(len(term1))
        
        index = len(term1) - 1
        extra = 0
        _sum = []
        
        while index >= 0:
            _sum.insert(0, (term1[index] + term2[index] + extra) % base)
            extra = (term1[index] + term2[index] + extra) // base
            index -= 1
        
        if extra != 0:
            _sum.insert(0, extra)
        
        return Number(self._listIntToBaseString(_sum), base)
        
    def _subtraction(self, term1, term2, base): 
        pass
    def _multiplication(self, factor1, factor2, base):
        pass
    def _division(self, divident, divisor, base):
        pass
    
    def _listIntToBaseString(self, listInt):
        baseString = ""
        for digit in listInt:
            if digit >= 0 and digit <= 9:
                baseString += str(digit)
            else:
                baseString += chr(digit + (ord('A') - 10))
        
        return baseString
    
    # validations
    
    def checkValidOption(self, opt, maxValue):
        return self._validator.checkValidOption(opt, maxValue)
    def checkValidBase(self, base):
        return self._validator.checkValidBase(base)
    def checkValidNumber(self, number, base):
        return self._validator.checkValidNumber(number, base)
