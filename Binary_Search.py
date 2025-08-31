class Solution(object):
    def search(self, nums, target):
        f = len(nums) - 1
        i = 0
        while(i <= f):
            meio = (f + i) // 2

            if(nums[meio] == target):
                return meio
            elif(nums[meio] > target):
                f = meio - 1
            else:
                i = meio + 1
        return -1 
        
