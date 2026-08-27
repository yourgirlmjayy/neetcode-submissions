from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get frequency of numbers in array
        frequency = Counter(nums)
        # create array for sorting numbers based on frequency
        bucketSort = [[] for i in range(len(nums) + 1)]
        
        for num, freq in frequency.items():
            bucketSort[freq].append(num)

        topKelements = []

        for i in range(len(bucketSort) - 1, -1, -1):
            if len(topKelements) == k:
                return topKelements
            if bucketSort[i]:
                topKelements.extend(bucketSort[i])





        