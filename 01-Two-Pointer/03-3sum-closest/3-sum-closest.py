class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() # must be sorted!
        closest = float('inf')
        mindist = float('inf')

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1

            while l<r:

                cursum = nums[i]+nums[l]+nums[r]
                
                if cursum == target:
                    return cursum

                elif cursum < target:
                    dist = abs(target-cursum)
                    if dist<mindist:
                        mindist = dist
                        closest = cursum

                    l+=1

                else: # cursum > target
                    dist = abs(target-cursum)
                    if dist<mindist:
                        mindist = dist
                        closest = cursum

                    r-=1

        return closest
