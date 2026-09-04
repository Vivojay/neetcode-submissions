class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for s in strs: # runs m times (m := len(strs))
            counts = [0]*26
            for x in s:
                chr_ind = ord(x)-ord('a')
                counts[chr_ind] += 1
            counts = tuple(counts)
            if counts in out:
                out[counts].append(s)
            else:
                out[counts] = [s]

        return list(out.values())