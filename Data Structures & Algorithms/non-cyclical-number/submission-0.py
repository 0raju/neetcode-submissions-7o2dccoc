class Solution:
    def isHappy(self, n: int) -> bool:

        def calculation(number):
            squared_sum = 0
            while number !=0:
                rem = number%10
                squared_sum += rem*rem
                number = number//10
            
            return squared_sum

        track = [n]
        while n != 1:
            n = calculation(n)
            if n not in track:
                track.append(n)
            else:
                return False
            # n = squared_sum
        
        return True

        
