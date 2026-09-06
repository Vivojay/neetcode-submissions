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
        s = self.make_dict(s1)
        l1 = len(s1)
        for i in range(len(s2)):
            if s == self.make_dict(s2[i:i+l1]):
                return True

        return False
