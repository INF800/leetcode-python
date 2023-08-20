class Solution:
    
    def three_sum_smaller(self, nums, max_sum):
        # `nums` is already sorted 

        # number of triplets with sum less than `max_sum`
        count = 0 
        
        for i in range(0, len(nums)-2):
            l = i+1
            r = len(nums)-1
            
            while l<r:
                
                cursum = nums[i]+nums[l]+nums[r]
                
                if cursum>=max_sum:
                    r-=1
                else:
                    count+=(r-l)
                    l+=1
                    
        return count
        
    
    def countTriplets(self, nums, N, L, R):
        
        nums.sort()
        
        # `count` is number of triplets having a sum in the range [L, R].
        count = self.three_sum_smaller(nums, R+1) - self.three_sum_smaller(nums, L)
        
        return count
