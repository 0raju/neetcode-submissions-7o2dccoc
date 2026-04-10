class Solution:
    def countSeniors(self, details: List[str]) -> int:

        counter = 0

        for p in details:
            if int(p[11:13]) > 60:
                counter+=1
        return counter
        