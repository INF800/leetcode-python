class Solution:
    def countTriplets(self, nums, n, sumo):
    
        nums.sort()
        count = 0 # number of triplets wth sum less than given value of sum `sumo`
        
        for i in range(len(nums)-1):
            l = i+1
            r = len(nums)-1
            
            while l<r:
                
                cursum = nums[i]+nums[l]+nums[r]
                
                if cursum>=sumo:
                    r-=1
                else:
                    count+=(r-l) # why not +=1? 
                    l+=1
                    
        return count
            
