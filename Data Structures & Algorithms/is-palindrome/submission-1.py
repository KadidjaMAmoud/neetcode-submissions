class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.replace(' ','')

        for x in s:
            if not x.isalnum():
                s =  s.replace(x,'')

        if len(s) == 0 or len(s) == 1:
            return True
        else:
            s = s.lower()
            if len(s) % 2 == 0: 
                middle = int(len(s) / 2)
                for x in range(middle):
                    opp = len(s)-1-x
                    if s[x] != s[opp]:
                        return False
                return True
            else:
                middle = int((len(s)-1)/2)
                for x in range(middle):
                    opp = 2 * middle - x
                    if s[x] != s[opp]:
                        return False
                return True
