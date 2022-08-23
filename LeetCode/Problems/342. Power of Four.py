import math
class Solution:
    def isPowerOfFour(self, n):
        if n <= 0:
            return False

        temp1 = math.log(n, 4)
        temp2 = int(temp1)

        if temp1 - temp2 == 0:
            return True
        else:
            return False
