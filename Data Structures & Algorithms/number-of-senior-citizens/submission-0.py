class Solution:
    def countSeniors(self, details: List[str]) -> int:

        counter = 0

        for p in details:
            yr = int(p[11:13])
            if yr>60:
                counter+=1
        return counter
        