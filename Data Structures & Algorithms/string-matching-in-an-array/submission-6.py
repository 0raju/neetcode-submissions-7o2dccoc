class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        # words = sorted(words, key=len)
        # right = len(words)-1

        # res = set()
        # for i in range(len(words)-1):
        #     for j in reversed(range(i+1, len(words))):
        #         if words[i] in words[j]:
        #             if words[i] not in res:
        #                 res.add(words[i])
        #                 break

        joined = " ".join(words)
        res = set()
        for w in words:
            if joined.count(w) > 1:
                res.add(w)
                
        return list(res)
        