class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(cur_string: str) -> bool:
            l = 0
            r = len(cur_string) - 1

            while(l < r):
                if(cur_string[l] != cur_string[r]):
                    return False
                
                l += 1
                r -= 1
            
            return True

        def recurse(cur_string: str, cur_list: List[str]) -> None:
            if(cur_string == ''):
                res.append(cur_list.copy())
                return
            
            for i in range(len(cur_string)):
                substring = cur_string[: i + 1]
                if( not is_palindrome(substring)):
                    continue
                
                cur_list.append(substring)
                next_string = cur_string[i + 1 : ] if i + 1 != len(cur_string) else ''
                recurse(next_string, cur_list)
                cur_list.pop()
            
            return

        recurse(s, [])        

        return res