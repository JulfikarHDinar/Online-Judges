class Solution:
    def leadingZero(self, aBin):
        for i in range (16 - len(aBin)):
            aBin = '0' + aBin       #leading zero

        return aBin

    def onesComplement16bit(self, binNum):
        for i in range (16 - len(binNum)):
            binNum = '0' + binNum       #leading zero
        #print(binNum)
        newBinNum = ''
        for i in range(len(binNum)):    #changing bit from left to right
            if binNum[i] == '0':
                newBinNum = newBinNum + '1'
            elif binNum[i] == '1':
                newBinNum = newBinNum + '0'
        return newBinNum

    def twosComplement16bit(self, binNum):
        binNum = self.onesComplement16bit(binNum)
        #print(binNum)
        newBinNum = ''
        carry = '1'
        for i in range(len(binNum)-1,-1,-1):
            if binNum[i] == '0' and carry == '0':
                newBinNum = '0' + newBinNum
                carry = '0'

            elif binNum[i] == '1' and carry == '0':
                newBinNum = '1' + newBinNum
                carry = '0'

            elif binNum[i] == '0' and carry == '1':
                newBinNum = '1' + newBinNum
                carry = '0'

            elif binNum[i] == '1' and carry == '1':
                newBinNum = '0' + newBinNum
                carry = '1'

        #print(newBinNum)

        return newBinNum

    def getSum(self, a, b):
        if a < 0:
            a = abs(a)
            aBin = format(a, 'b')
            aBin = self.twosComplement16bit(aBin)
        else:
            aBin = format(a, 'b')   #binary 
            aBin = self.leadingZero(aBin)

        if b < 0:
            b = abs(b)
            bBin = format(b, 'b')
            bBin = self.twosComplement16bit(bBin)
        else:
            bBin = format(b, 'b')   #binary 
            bBin = self.leadingZero(bBin)
            
        #print(aBin, bBin)
        
        res = ''
        carry = '0'

        for i in range(15,-1,-1):
            if aBin[i] == '0' and  bBin[i] == '0' and carry == '0':
                res = '0' + res 
                carry = '0'

            elif aBin[i] == '0' and  bBin[i] == '0' and carry == '1':
                res = '1' + res 
                carry = '0'

            elif ((aBin[i] == '0' and  bBin[i] == '1') or (aBin[i] == '1' and  bBin[i] == '0'))  and carry == '0':
                res = '1' + res 
                carry = '0'

            elif ((aBin[i] == '0' and  bBin[i] == '1') or (aBin[i] == '1' and  bBin[i] == '0'))  and carry == '1':
                res = '0' + res 
                carry = '1'
            
            elif aBin[i] == '1' and  bBin[i] == '1' and carry == '0':
                res = '0' + res 
                carry = '1'

            elif aBin[i] == '1' and  bBin[i] == '1' and carry == '1':
                res = '1' + res 
                carry = '1'

        #print(res)

        if res[0] == '1':   #sign bit
            res = self.twosComplement16bit(res)
            return -int(res, 2)

        else:
            return int(res, 2)