class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check that lengths of strings match
        if len(s) != len(t):
            return False

        def freq_counter(string):
            counter = {}
            for char in string:
                if char in counter:
                    counter[char] += 1
                else:
                    counter[char] = 1
            return counter
        
        s_counter = freq_counter(s) 
        t_counter = freq_counter(t)

        for key, value in s_counter.items():
            if key in t_counter:
                if t_counter[key] != value:
                    return False
            else:
                return False
        return True

                

            
            
        
        