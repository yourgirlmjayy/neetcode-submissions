class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
            elif nums[i] == 0:
                if curr > result:
                    result = curr
                curr = 0
        if curr > result: 
            result = curr
        return result