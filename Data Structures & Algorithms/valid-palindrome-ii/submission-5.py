class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        def is_palindrome(left: int, right: int) -> bool:
            
            while(left < right):
                if(s[left] != s[right]):
                    return False
                left += 1
                right -= 1
            return True

        while (l < r):
            if(s[l] != s[r]):
                return is_palindrome(l, r - 1) or is_palindrome(l + 1, r)
            
            l += 1
            r -= 1
        
        return True