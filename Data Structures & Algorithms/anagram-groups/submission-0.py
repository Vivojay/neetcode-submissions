class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = dict()

        for i, j in [(''.join(sorted(i)), i) for i in strs]:
            if i in x:
                x[i].append(j)
            else:
                x[i]=[j]

        return list(x.values())
