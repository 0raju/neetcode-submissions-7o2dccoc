class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len)

        res = []
        right = len(words)-1

        for i in range(len(words)-1):
            for j in reversed(range(i+1, len(words))):
                if words[i] in words[j]:
                    if words[i] not in res:
                        res.append(words[i])

        return res
        