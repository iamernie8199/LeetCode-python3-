"""
Given a non-negative integer num,
return the number of steps to reduce it to zero.
If the current number is even, you have to divide it by 2,
otherwise, you have to subtract 1 from it.
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 1
        while num >= 2:
            if num % 2 != 0:
                count += 2
            else:
                count += 1
            num = num//2
        return count
