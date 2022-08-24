import math
from decimal import Decimal, getcontext

class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        elif n == 1:
            return True

        getcontext().prec = 11
        temp1 = Decimal(math.log(n))/Decimal(math.log(3))       #math.log(x, b)'s calculation is log(x) / log(b)
        temp2 = int(temp1)

        if temp1-temp2 == 0:
            return True
        else: 
            return False