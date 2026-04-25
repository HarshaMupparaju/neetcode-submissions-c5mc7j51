class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

        n = len(arr)

        max_right = -1

        for i in range(n - 1, -1, -1):
            temp = max_right
            max_right = max(max_right, arr[i])
            arr[i] = temp
        
        arr[-1] = -1
        return arr