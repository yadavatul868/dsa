# Link - https://www.youtube.com/watch?v=jJXJ16kPFWg


# only consider alpha numeric characters
# ignore cases of character

# Code
class Solution:

    def isPalindrome(self, s):

        l, r = 0, len(s)-1
        while l <= r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # print(str(l) + ':' + str(r))
            # print(str(s[l]) + ':' + str(s[r]))
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        
        return True



    def alphaNum(self, c):

        isAlphaNum = False
        if ord('A') <= ord(c) <= ord('Z'):
            isAlphaNum = True
        elif ord('a') <= ord(c) <= ord('z'):
            isAlphaNum = True
        elif ord('0') <= ord(c) <= ord('9'):
            isAlphaNum = True
        
        return isAlphaNum
    
# Run

if __name__ == '__main__':

    S = Solution()
    S.isPalindrome('A man, a plan, a canal: panama')




































