class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        res = [] # option-1

        for i in range(len(blocks)-k+1):
            res.append(blocks[i:i+k].count('W'))
        
        return min(res)
        
        # curr = blocks[:k].count('W')
        # res = curr

        # for i in range(k, len(blocks)):
        #     if blocks[i] == 'W':
        #         curr += 1
        #     if blocks[i - k] == 'W':
        #         curr -= 1
        #     res = min(res, curr)
        
        # return res
