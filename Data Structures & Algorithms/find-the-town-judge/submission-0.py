class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj_list = {i : set() for i in range(1, n + 1)}

        for e in trust:
            ai = e[0]
            bi = e[1]

            adj_list[ai].add(bi)

        judge_candidates = []
        for k in adj_list:
            if(len(adj_list[k]) == 0):
                judge_candidates.append(k)

        if(len(judge_candidates) > 1 or len(judge_candidates) == 0):
            return -1
        
        possible_judge = judge_candidates[0]

        for key in adj_list:
            if(key == possible_judge):
                continue
            
            if(possible_judge not in adj_list[key]):
                print('here')
                return -1
        
        return possible_judge