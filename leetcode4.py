def findMedianSortedArrays(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        nums1 = sorted(nums1+nums2)
        m=len(nums1)
        if m%2 == 1:
            median = nums1[m//2]
            return round(median, 5)
        else:
            median = (nums1[m//2 -1] + nums1[m//2])/2.0
            return round(median, 5)
