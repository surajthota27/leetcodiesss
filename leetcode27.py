class Solution(object):
    def removeElement(self, nums, val):
        for num in nums:
            if num == val:
                nums.pop(num)
        return nums
obj = Solution()
nums=list(map(int,input('Enter a list of numbers: ')))
val=int(input('Enter a value'))
print(obj.removeElement(nums,val))  