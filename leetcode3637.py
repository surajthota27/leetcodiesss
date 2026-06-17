nums = list(map(int,input('enter a list: ').split(' ')))
if len(nums)>3:
    i,i_start=0,0
    while i<len(nums)-1 and nums[i]<nums[i+1]:
        i+=1
    if i_start<i:   
        p,p_start=i,i
        while p<len(nums)-1 and nums[p]>nums[p+1]:
            p+=1
        if p_start<p:
            q,q_start=p,p
            while q<len(nums)-1 and nums[q]<nums[q+1]:
                q+=1
            if q_start<q:
                if q==len(nums)-1:
                    print(True)
                
print(False)
