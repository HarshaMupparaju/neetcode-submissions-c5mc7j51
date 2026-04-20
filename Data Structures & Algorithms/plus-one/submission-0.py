class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        res = []

        for i in range(len(digits) - 1, -1, -1):
            res.append((digits[i] + carry) % 10)
            carry = (digits[i] + carry) // 10
        
        if(carry != 0):
            res.append(carry)

        res.reverse()

        return res