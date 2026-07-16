class Solution:
    def isPalindrome(self, s: str) -> bool:
        #TC: O(n), SC: O(n)
        
        temp = []
        for c in s:
            if( (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')) or (ord('0') <= ord(c) <= ord('9')) ):
                temp.append(c.lower())
        
        s = ''.join(temp)

        left = 0
        right = len(s) - 1

        while(left <= right):
            if(s[left] != s[right]):
                return False
            
            left += 1
            right -= 1

        return True