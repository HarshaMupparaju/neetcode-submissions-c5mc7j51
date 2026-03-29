class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        count = 0

        def decode(s: str, i: int, j: int) -> None:
            nonlocal count

            if(i >= j):
                count += 1
                return
            
            if(s[i] != '0'):
                decode(s, i + 1, j)
            
            if(i + 1 < n and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456')):
                decode(s, i + 2, j)
            
            return


        decode(s, 0, n)

        return count