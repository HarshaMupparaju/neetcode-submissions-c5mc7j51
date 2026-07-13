class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr1: List[int], arr2: List[int]) -> List[int]:
            res = []

            start1 = 0
            start2 = 0

            while(start1 < len(arr1) and start2 < len(arr2)):
                if(arr1[start1] <= arr2[start2]):
                    res.append(arr1[start1])
                    start1 += 1
                else:
                    res.append(arr2[start2])
                    start2 += 1
            
            while(start2 < len(arr2)):
                res.append(arr2[start2])
                start2 += 1
            
            while(start1 < len(arr1)):
                res.append(arr1[start1])
                start1 += 1
            
            return res


        def sort(start: int, end: int) -> List[int]:
            if(end - start == 1):
                return nums[start: end]
            
            mid = (start + end) // 2

            left = sort(start, mid)
            right = sort(mid , end)

            res = merge(left, right) 
            
            return res
            


        res = sort(0, len(nums))

        return res