class Solution:
    def isValid(self, s: str) -> bool:
        #TC: O(n); SC: O(n)
        stack = []
        res = True

        for c in s:
            if(c in ['(', '[', '{']):
                stack.append(c)
            else:
                if(stack):
                    top = stack[-1]
                    if((top == '(' and c == ')') or (top == '[' and c == ']') or (top == '{' and c == '}') ):
                        stack.pop()
                    else:
                        res = False
                        break
                else:
                    res = False
        
        if stack:
            res = False
        
        return res