class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_new = "".join(c.lower() for c in s if c.isalnum())
        print(s_new)
        for i in range(len(s_new) // 2):
            if(s_new[i] != s_new[len(s_new) - 1 - i]):
                return False

        return True