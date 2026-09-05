class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        i = 0
        j = l-1

        alnum = lambda x: (x.lower() >= 'a' and x.lower() <= 'z') or (x.lower() >= '0' and x.lower() <= '9')

        while i < j:
            low = s[i].lower()
            high = s[j].lower()

            if not alnum(low):
                i+=1
                continue
            if not alnum(high):
                j-=1
                continue

            if low != high:
                return False

            i+=1
            j-=1

        return True


