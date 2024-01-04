def productExceptSelf(nums):

        
        pre = [1]
        suf = [1]
        buf = 1
        for i in range(1, len(nums)):
            buf *= nums[i-1]
            pre.append(buf)

        buf = 1
        for i in range(len(nums)-2,-1,-1):
            buf *= nums[i+1]
            suf.append(buf)

        
        res = []
        for i in range(len(nums)):
            res.append(pre[i] * suf[len(nums)-i-1])

        
        return res


productExceptSelf([1,2,3,4])