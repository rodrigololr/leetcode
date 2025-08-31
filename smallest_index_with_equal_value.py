class Solution(object):
    def smallestEqual(self, nums):
        n = len(nums)
        for x in range(n):
            if(x % 10 == nums[x]):
                return x
        return -1
        
