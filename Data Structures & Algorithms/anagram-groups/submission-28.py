class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for s in strs: # runs m times (m := len(strs))
            counts = [0]*26
            for x in s:
                chr_ind = ord(x)-ord('a')
                counts[chr_ind] += 1

            if tuple(counts) in out:
                out[tuple(counts)].append(s)
            else:
                out[tuple(counts)] = [s]

        return list(out.values())