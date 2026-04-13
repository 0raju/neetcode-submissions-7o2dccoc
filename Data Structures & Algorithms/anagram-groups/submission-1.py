from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram[sorted_s].append(s)
        res = []
        for value in anagram.values():
            res.append(value)
        return res


        
        