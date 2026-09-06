class Solution:
    def make_dict(self, l: list) -> dict:
        d = {}
        for i in l:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return d

    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        s1d = self.make_dict(s1)
        s2d = self.make_dict(s2[:l1])


        # s1 = "abc", s2 = "lecaabee"
        for i in range(l1, l2):
            if s1d == s2d:
                return True

            if s2d[s2[i-l1]] == 1: del s2d[s2[i-l1]]
            else: s2d[s2[i-l1]] -= 1

            if s2[i] in s2d: s2d[s2[i]] += 1
            else: s2d[s2[i]] = 1

        if s1d == s2d:
            return True

        return False
