class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        res = 0
        people.sort()
        n =len(people)
        left = 0
        right = n-1

        while left < right:
            if people[left] + people[right] <= limit:
                left+=1
            res+=1
            right-=1
        
        if left==right:
            res+=1
        return res
            

        



        