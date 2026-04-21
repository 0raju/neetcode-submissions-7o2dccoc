class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return True

        n_s1 = len(s1)
        freq_s1 = {c: s1.count(c) for c in s1}
        res = False

        for i in range(0, len(s2)-1):
            sub_str = s2[i:i+n_s1]
            freq_s2 = {c: sub_str.count(c) for c in sub_str}

            if freq_s1==freq_s2:
                res= True

        return res



        