from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        # get the length of the ith item in string and add delimiter
        # apple ben love -> 5#apple3#ben4#love
        encodedString = ""
        for s in strs:
            tmpStr = str(len(s)) + "#" + s
            encodedString += tmpStr

        return encodedString

    def decode(self, s: str) -> List[str]:
        # 5#apple3#ben4#love -> apple ben love

        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            ans.append(s[i:j])
            i = j

        return ans
