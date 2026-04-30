class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []

        for op in operations:
            if(op == '+'):
                s1 = st.pop()
                s2 = st[-1]
                
                st.append(s1)

                st.append(int(s1) + int(s2))
            elif(op == 'D'):
                s1 = st[-1]
                st.append(int(s1) * 2)
            elif(op == 'C'):
                s1 = st.pop()
            else:
                st.append(op)
        
        res = 0
        while(st):
            s1 = st.pop()
            res += int(s1)
        
        return res