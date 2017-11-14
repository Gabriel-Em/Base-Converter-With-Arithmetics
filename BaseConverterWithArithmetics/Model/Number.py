class Number:
    def __init__(self, value, base):
        value = self._trim(value)
        self._digitsAsListOfInt = self._valueToListInt(value)
        self._digitsAsListOfChar = self._valueToListChar(value)
        self._base = base
        self._length = len(self._digitsAsListOfInt)
        
    def getNumberAsListOfInt(self):
        return self._digitsAsListOfInt
    
    def getNumberAsListOfChar(self):
        return self._digitsAsListOfChar
    
    def getBase(self):
        return self._base
    
    def lengthen(self, newLength):
        if newLength > self._length:
            for _ in range(newLength - self._length):
                self._digitsAsListOfInt.insert(0, 0)
                self._digitsAsListOfChar.insert(0, '0')
            self._length = newLength
            
    def __str__(self):
            return ''.join(self._digitsAsListOfChar)
    
    def __len__(self):
        return self._length
    
    def __getitem__(self, key):
        return self._digitsAsListOfInt[key]
        
    def _valueToListChar(self, value):
        listOfChar = []
        for digit in value:
            listOfChar.append(digit)
        
        return listOfChar
    
    def _valueToListInt(self, value):
        listOfInt = []
        for digit in value:
            listOfInt.append(self._charToInt(digit))
        
        return listOfInt
    
    def _charToInt(self, char):
        if char >= '0' and char <= '9':
            return int(char)
        else:
            return ord(char) - (ord('A') - 10)
    
    def _trim(self, value):
        while len(value) > 1 and value[0] == '0':
            value = value[1:]
        return value