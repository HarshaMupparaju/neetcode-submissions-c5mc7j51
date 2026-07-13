class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(f'{len(s)}#{s}')
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while(i < len(s)):
            num_chars = []

            while(s[i] != '#'):
                num_chars.append(s[i])
                i += 1
            
            num_chars = int(''.join(num_chars))

            i += 1

            word = s[i: i + num_chars]

            res.append(word)

            i += num_chars

        return res
