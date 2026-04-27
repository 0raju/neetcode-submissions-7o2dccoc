class Solution:
    def isHappy(self, n: int) -> bool:

        def calculation(number):
            squared_sum = 0
            while number !=0:
                rem = number%10
                squared_sum += rem*rem
                number = number//10
            
            return squared_sum

        track = set()
        while n != 1:
            if n in track:
                return False
            track.add(n)
            n = calculation(n)
        
        return True

        
