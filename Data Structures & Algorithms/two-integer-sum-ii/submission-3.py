class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #TC: O(n log n); SC: O(1)
        #Binary Search
        def binary_search(element: int) -> int:
            l = 0
            r = len(numbers) - 1

            while(l <= r):
                m = (l + r) // 2

                if(numbers[m] == element):
                    return m
                elif(numbers[m] < element):
                    l = m + 1
                else:
                    r = m - 1
                
            return -1

        #Iterate through each element and do binary_search(target - cur)
        for i, num in enumerate(numbers):
            second_idx = binary_search(target - num)

            if(second_idx != -1 and i != second_idx):
                return [min(i, second_idx) + 1, max(i, second_idx) + 1]
        
        #Return
        return -1