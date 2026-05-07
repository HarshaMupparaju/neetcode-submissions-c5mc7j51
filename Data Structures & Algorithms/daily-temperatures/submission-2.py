class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_st = [] # As we want the next highest, we use a monotonically decreasing stack, (temp, index)

        res = []

        for i in range(len(temperatures) - 1, -1, -1):
            while(mono_st and mono_st[-1][0] <= temperatures[i]):
                mono_st.pop()
            
            if(len(mono_st) == 0):
                res.append(0)
            else:
                res.append(mono_st[-1][1] - i)
            
            mono_st.append((temperatures[i], i))

        res.reverse()
        return res