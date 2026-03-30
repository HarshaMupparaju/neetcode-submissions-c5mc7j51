class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if(token == '+' or token == '-' or token == '*' or token == '/'):
                num2 = st.pop()
                num1 = st.pop()

                if(token == '+'):
                    res = num1 + num2
                elif(token == '-'):
                    res = num1 - num2
                elif(token == '*'):
                    res = num1 * num2
                else:
                    res = int(num1 / num2)
                
                print(res)
                st.append(res)
            else:
                st.append(int(token))
        
        return st[-1]