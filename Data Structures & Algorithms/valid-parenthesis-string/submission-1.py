class Solution:
    def checkValidString(self, s: str) -> bool:
        para_st = []
        star_st = []

        for i, c in enumerate(s):
            if(c == '('):
                para_st.append((c, i))
            elif(c == ')'):
                if(len(para_st) > 0):
                    para_st.pop()
                elif(len(star_st) > 0):
                    star_st.pop()
                else:
                    return False
            else:
                star_st.append((c, i))
        
        #Process the rest of para_st
        while(len(para_st) > 0):
            if(len(star_st) == 0 or para_st[-1][1] > star_st[-1][1]):
                return False
            para_st.pop()
            star_st.pop()
            
        return True
