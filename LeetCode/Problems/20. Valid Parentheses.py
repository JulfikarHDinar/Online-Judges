class Solution:
    def isValid(self, s: str) -> bool:
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


          

