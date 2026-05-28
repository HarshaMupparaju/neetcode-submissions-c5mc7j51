class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if(num1 == '0' or num2 == '0'):
            return '0'
        
        temp = []
        for i in range(len(num2) - 1, -1, -1):
            carry = 0
            s = ''
            for j in range(len(num1) - 1, -1, -1):
                mult = int(num2[i]) * int(num1[j]) + carry
                carry = mult // 10
                s += str(mult % 10)
            
            if(carry > 0):
                s += str(carry)

            s = s[::-1]
            
            if(len(num2) - 1 - i > 0):
                for k in range(len(num2) - 1 - i):
                    s += '0'
            
            temp.append(s)
        

        # print(temp)

        ##Add all the sums in temp together
        res = ''

        longest = 0
        for s in temp:
            longest = max(len(s), longest)
        
        # print(longest)

        temp2 = []
        for s in temp:
            while(len(s) < longest):
                s = '0' + s
            
            # s = s[::-1]
            temp2.append(s)
        
        # print(temp2)

        carry = 0

        for i in range(longest - 1, -1, -1):
            add = 0
            for s in temp2:
                add += int(s[i])
            
            add += carry
            carry = add // 10
            res += str(add % 10)
            # print(add)
            # print(1/0)

        res += str(carry)
        res = res[::-1]

        for i in range(len(res)):
            if(res[i] != '0'):
                res = res[i:]
                break

        return res
