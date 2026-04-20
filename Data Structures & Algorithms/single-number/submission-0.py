class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res = res ^ num # All 2-repeated numbers iwll zero out as XOR is commutative
        
        return res