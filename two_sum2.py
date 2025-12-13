# Link : https://www.youtube.com/watch?v=cQ1Oz4ckceM


# given is a array of integrer which is already sorted in aescending order
# find index of two numbers which add up to a specific target
# both index1 and index2 are non-zero, index1 < index2

# can't use same element twice
# each input has exactly one solution


# Code


class Solution:

    def twoSum(self, numbers, target):

        l, r = 0, len(numbers)-1

        while l < r:

            curSum = numbers[l] + numbers[r]
            
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [(l + 1), (r + 1)]
            

# Run

if __name__ == '__main__':
    S = Solution()
    S.twoSum([1,3,4,5,7,11], 9)






            



