class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        res = []

        for i in range(len(blocks)-k+1):
            res.append(blocks[i:i+k].count('W'))
        
        return min(res)
        