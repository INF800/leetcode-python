class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)-2):

            # skip duplicates
            if i>0 and nums[i-1]==nums[i]:
                continue

            l=i+1
            r=len(nums)-1

            while l<r:
                cursum = nums[i]+nums[l]+nums[r]
                if cursum==0:
                    triplets.append(
                        [nums[i], nums[l], nums[r]]
                    )

                    l+=1
                    r-=1

                    # skip duplicates
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    
                    # skip duplicates
                    while l<r and nums[r]==nums[r+1]:
                        r-=1

                elif cursum < 0:
                    l+=1
                
                else:
                    r-=1

        return triplets
                    
