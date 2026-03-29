class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while(start < end):
            if(numbers[start] + numbers[end] == target):
                #Adjust to 1-indexing
                return [start + 1, end + 1]
            elif(numbers[start] + numbers[end] > target):
                end -= 1
            else:
                start += 1
        
        print(f'Oops, sth went wrong!')
        return [-1, -1]