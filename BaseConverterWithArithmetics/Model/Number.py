class Number:
    def __init__(self, value, base):
        self._digitsAsListOfInt = self._valueToListInt(value)
        self._digitsAsListOfChar = self._valueToListChar(value)
        self._base = base
    
    def getNumberAsListOfInt(self):
        return self._digitsAsListOfInt
    
    def getNumberAsListOfChar(self):
        return self._digitsAsListOfChar
    
    def getBase(self):
        return self._base
    
    def __str__(self):
            return ''.join(self._digitsAsListOfChar)
        
    def _valueToListChar(self, value):
        listOfChar = []
        for digit in value:
            listOfChar.append(digit)
        
        return list
    
    def _valueToListInt(self, value):
        listOfInt = []
        for digit in value:
            listOfInt.append(self._charToInt(digit))
    
    def _charToInt(self, char):
        if char >= '0' and char <= '9':
            return int(char)
        else:
            return ord(char) - 'A'