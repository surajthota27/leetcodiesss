class Solution(object):
    
        def removeDuplicates(self,nums):
            nums1=[]
            for x in nums:
                if x not in nums1:
                    nums1.append(x)     
            return sorted(nums1,reverse=0),len(nums1)
obj = Solution()
nums=list(map(int,input('Enter a list of numbers: ')))
print(obj.removeDuplicates(nums))