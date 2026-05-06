class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for a in asteroids:
            while(st and a < 0 and st[-1] > 0):
                if(a + st[-1] < 0):
                    #a wins
                    st.pop()
                elif(a + st[-1] > 0):
                    #st[-1] wins
                    a = 0
                else:
                    # a and st[-1] are same size
                    a = 0
                    st.pop()
            
            if(a != 0):
                st.append(a)

        return st