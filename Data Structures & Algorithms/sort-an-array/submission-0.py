class Solution:
    def mergeSorted(self, arr1: List[int], arr2: List[int]) -> List[int]:
        temp = []
        arr1_ptr = 0
        arr2_ptr = 0

        while(arr1_ptr < len(arr1) and arr2_ptr < len(arr2)):
            if(arr1[arr1_ptr] <= arr2[arr2_ptr]):
                temp.append(arr1[arr1_ptr])
                arr1_ptr += 1
            else:
                temp.append(arr2[arr2_ptr])
                arr2_ptr += 1

        if(arr1_ptr >= len(arr1)):
            ptr = arr2_ptr
            arr = arr2
        else:
            ptr = arr1_ptr
            arr = arr1
        
        while(ptr < len(arr)):
            temp.append(arr[ptr])
            ptr += 1
        
        return temp
        


    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        print(nums)

        if(n == 1):
            return nums
        
        arr1 = nums[ : (n // 2)]
        arr2 = nums[(n // 2) : ]

        sorted_arr1 = self.sortArray(arr1)
        sorted_arr2 = self.sortArray(arr2)

        return self.mergeSorted(sorted_arr1, sorted_arr2)