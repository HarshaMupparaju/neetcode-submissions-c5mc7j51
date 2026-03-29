class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        start_ptr = 0
        end_ptr = len(people) - 1
        people_sorted = sorted(people)

        num_boats = 0

        temp = 0
        num_people = 0
        while(start_ptr <= end_ptr):
            if(num_people == 2):
                num_boats += 1
                temp = 0
                num_people = 0

            if(temp + people_sorted[end_ptr] <= limit):
                temp += people_sorted[end_ptr]
                num_people += 1
                end_ptr -= 1
            elif(temp + people_sorted[start_ptr] <= limit):
                temp += people_sorted[start_ptr]
                num_people += 1
                start_ptr += 1
            else:
                num_boats += 1
                temp = 0
                num_people = 0
        
        if(temp != 0):
            num_boats += 1
        
        return num_boats
        