class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        res = 0

        for num in nums:
            s.add(num)
        
        for num in nums:
            if(num - 1 in s):
                continue
            temp = num
            curr_sequence = 1
            res = max(res, curr_sequence)
            while(temp + 1 in s):
                temp = temp + 1
                curr_sequence += 1
                res = max(res, curr_sequence)
        
        return res

