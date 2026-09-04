import math

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # transform = lambda x: 2**(ord(x)-ord('a'))
        transform = lambda x: 2**(ord(x)-ord('a')) - math.sin(ord(x))
        c = {}

        for i in strs:
            s = sum([transform(x) for x in i])
            if (s, len(i)) in c:
                c[(s, len(i))].append(i)
            else:
                c[(s, len(i))] = [i]

        return list(c.values())
