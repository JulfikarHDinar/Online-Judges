from itertools import combinations
class Solution(object):
    def generateParenthesis(self, n):

        m=n*2
        arr=list(range(1,m,1))

        arrCom = combinations(arr, n)
        posBrc = []
        for i in list(arrCom):
            if i[0] == 1:
                posBrc.append(i)

        #print(posBrc)
        genBrc =[]
        for ncom in posBrc:
            #print(ncom)
            a = []
            for i in range(1,m+1,1):
                if i in ncom:
                    a.append('(')
                else: 
                    a.append(')')

            a = ''.join(map(str, a))
            genBrc.append(a)

        #print(genBrc)
        validBrc = []
        for i in genBrc:
            if self.validPar(i) == True:
                validBrc.append(i)
        return validBrc
        
    def validPar(self, s):
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)

            elif i == '{':
                stack.append(i)

            elif i == '[':
                stack.append(i)

            elif i == ')':
                if len(stack) == 0:
                    return False
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)

            elif i == '}':
                if len(stack) == 0:
                    return False
                if stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(i)

            elif i == ']':
                if len(stack) == 0:
                    return False
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(i)

        if len(stack) == 0:
            return True
        else:
            return False