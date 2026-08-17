class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        def convert_to_letter(num: int) -> str:
            char = ord('A') + (num - 1)
            return chr(char)

        while(columnNumber > 26):

            reminder = columnNumber % 26

            res.append(convert_to_letter(reminder))

            columnNumber = columnNumber // 26

        if(columnNumber > 0):
            res.append(convert_to_letter(columnNumber))

        res.reverse()
        return ''.join(res)