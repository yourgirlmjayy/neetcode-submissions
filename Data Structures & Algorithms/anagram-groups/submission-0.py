from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            # convert count to immutable data structure
            key = tuple(count)
            group_anagrams[key].append(s)
        
        return list(group_anagrams.values())
        