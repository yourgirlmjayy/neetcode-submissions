class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string  
        return encoded_string             

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        decoded = []
        delimiter = "#"
        # j should be less than the len of s
        i = 0
        j = 0
        str_len = ""
        
        while i < len(s):
            #keep track of the string's length until you get to the delimiter
            if s[j] != delimiter:
                str_len += str(s[j])
                j += 1
            else: 
                # convert str length to int
                stop = j + 1 + int(str_len)
                decoded.append(str(s[j + 1:stop]))

                i = stop
                j = i
                str_len = ""

        return decoded



        
