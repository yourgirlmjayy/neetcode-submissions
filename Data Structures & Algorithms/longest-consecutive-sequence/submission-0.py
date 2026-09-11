class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set to get rid of duplicates
        nums_set = set(nums)
        max_length = 0

        for num in nums_set:
            curr_length = 0 
            # check if num is the largest 
            # num in the sequence
            if num + 1 not in nums_set:
                curr_length = 1
                n = num
                # find the smallest number in the sequence
                while n - 1 in nums_set:
                    curr_length +=1 
                    n -= 1
            #update max length
            max_length = max(curr_length, max_length)

        return max_length

        