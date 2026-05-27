class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if(len(A) > len(B)):
            A, B = B, A
        
        n = len(nums1) + len(nums2)

        half = n // 2

        l = 0
        r = len(A) - 1
        
        res = 0

        while True:
            i = (l + r) // 2
            j = half - (i + 1) - 1

            A_left = A[i] if i >= 0 else float('-inf')
            A_right = A[i + 1] if (i + 1) < len(A) else float('inf')

            B_left = B[j] if j >= 0 else float('-inf')
            B_right = B[j + 1] if (j + 1) < len(B) else float('inf')

            #Valid partition
            if(A_left <= B_right and B_left <= A_right):
                if(n % 2 == 0):
                    res = (max(A_left, B_left) + min(A_right, B_right)) / 2
                else:
                    res = min(A_right, B_right)
            
                break
            elif(A_left > B_right):
                r = i - 1
            elif(B_left > A_right):
                l = i + 1
        
        return res
