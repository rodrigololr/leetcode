# Ordena a lista, fixa um número e usa dois ponteiros para achar trios que somem zero, pulando duplicatas.
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if( i > 0 and nums[i] == nums[i-1]):
                continue
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                soma = nums[i] + nums[left] + nums[right]

                if(soma == 0):
                    res.append([nums[i], nums[left], nums[right]])
                
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif(soma < 0):
                    left += 1
                elif(soma > 0):
                    right -= 1
        return res
