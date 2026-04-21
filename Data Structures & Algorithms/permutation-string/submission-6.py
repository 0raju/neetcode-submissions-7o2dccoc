class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # if s1 == s2: #option1
        #     return True

        # n_s1 = len(s1)
        # freq_s1 = {c: s1.count(c) for c in s1}
        # res = False

        # for i in range(0, len(s2)-1):
        #     sub_str = s2[i:i+n_s1]
        #     freq_s2 = {c: sub_str.count(c) for c in sub_str}

        #     if freq_s1==freq_s2:
        #         res= True

        # return res


        if len(s1)> len(s2): return False
        freq_s1 = {c: s1.count(c) for c in s1}
        window_s2 = {c: s2[:len(s1)].count(c) for c in s2[:len(s1)]}
        if freq_s1 == window_s2:
            return True
        
        for i in range(len(s1), len(s2)):
            window_s2[s2[i]] = window_s2.get(s2[i], 0) + 1
            drop = s2[i - len(s1)]
            window_s2[drop] -= 1
            if window_s2[drop] == 0:
                del window_s2[drop]
            
            if freq_s1==window_s2:
                return True
        
        return False






        