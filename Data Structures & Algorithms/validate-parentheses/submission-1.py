class Solution:
    def isValid(self, s: str) -> bool:
        A = []

        for i in range(len(s)):
            if(s[i] == '(' or s[i] == '{' or s[i] =='['):
                A.append(s[i])
            else:
                if(s[i] == ')' and len(A) > 0 and  A[-1] == '('):
                    A.pop()
                elif(s[i] == '}' and len(A) > 0 and A[-1] == '{'):
                    A.pop()
                elif(s[i] == ']' and len(A) > 0 and A[-1] == '['):
                    A.pop()
                else:
                    return False
        
        if(len(A) != 0):
            return False
        
        return True