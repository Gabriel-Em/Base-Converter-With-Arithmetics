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
            return "0"
        elif len(listOfTerms) == 1:
            return str(listOfTerms[0])
        else:
            sumOfTerms = self._addition(listOfTerms[0], listOfTerms[1], destinationBase)
            for i in range(2, len(listOfTerms)):
                sumOfTerms = self._addition(sumOfTerms, listOfTerms[i] , destinationBase)
            return str(sumOfTerms)
        
    
    def _conversionByRepeatedDivision(self, number, destinationBase):
        remainders = []
        
        while str(number) != "0":
            number, remainder = self._division(number, destinationBase, number.getBase())
            remainders.insert(0, remainder)
        
        return self._listIntToBaseString(remainders)        
        
    def quickConvertToBase2(self, strNumber, sourceBase):
        number = Number(strNumber, sourceBase)
        
        sizeOfGroup = 2
        while 2 ** sizeOfGroup != sourceBase:
            sizeOfGroup += 1
        
        convertedNumber = ""
        for digit in number.getNumberAsListOfChar():
            remainders = []
            digit = Number(digit, sourceBase)
            while str(digit) != '0':
                digit, remainder = self._division(digit, 2, sourceBase)
                remainders.insert(0, str(remainder))
            if len(remainders) == 0:
                remainders.append('0')
            convertedNumber += self.lengthen(sizeOfGroup, ''.join(remainders))
        
        return self.trim(convertedNumber)
        
        
    def quickConvertFromBase2(self, strNumber, destinationBase):
        number = Number(strNumber, 2)
        
        sizeOfGroup = 2
        while 2 ** sizeOfGroup != destinationBase:
            sizeOfGroup += 1
        
        if len(number) % sizeOfGroup != 0:
            number.lengthen(len(number) // sizeOfGroup * sizeOfGroup + sizeOfGroup)
        
        convertedNumber = ""
        for i in range(0, len(number) // sizeOfGroup):
            convertedNumber += self._conversionBySubstitution(Number(''.join(number.getNumberAsListOfChar()[i*sizeOfGroup:i*sizeOfGroup + sizeOfGroup]), 2), destinationBase)
        
        return convertedNumber
            
            
    # Arithmetic operations
    
    def _addition(self, term1, term2, base):
        if len(term1) < len(term2):
            term1.lengthen(len(term2))
        elif len(term1) > len(term2):
            term2.lengthen(len(term1))
        
        index = len(term1) - 1
        carry = 0
        _sum = []
        
        while index >= 0:
            _sum.insert(0, (term1[index] + term2[index] + carry) % base)
            carry = (term1[index] + term2[index] + carry) // base
            index -= 1
        
        if carry != 0:
            _sum.insert(0, carry)
        
        return Number(self._listIntToBaseString(_sum), base)
        
    def _subtraction(self, term1, term2, base): 
        pass
    def _multiplication(self, factor1, factor2, base):
        pass
    def _division(self, divident, divisor, base):
        quotient = []
        remainder = 0
        index = 0
        
        while index < len(divident):
            quotient.append((remainder * base + divident[index]) // divisor)
            remainder = (remainder * base + divident[index]) % divisor
            index += 1
        
        return Number(self._listIntToBaseString(quotient), base), remainder
    
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

    def trim(self, strNumber):
        while len(strNumber) > 1 and strNumber[0] == '0':
            strNumber = strNumber[1:]
        return strNumber
    
    def lengthen(self, newLength, strNumber):
        if newLength > len(strNumber):
            for _ in range(newLength - len(strNumber)):
                strNumber = "0" + strNumber
        return strNumber
