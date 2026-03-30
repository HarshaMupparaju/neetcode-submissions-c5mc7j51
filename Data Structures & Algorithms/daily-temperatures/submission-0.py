class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []

        res = []

        for i in range(len(temperatures) - 1, -1, -1):
            while(len(st) > 0 and st[-1][0] <= temperatures[i] ):
                st.pop()
            
            if(len(st) == 0):
                res.append(0)
            else:
                res.append(st[-1][1] - i)
            
            st.append([temperatures[i], i])
        
        res.reverse()

        return res