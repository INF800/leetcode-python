class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_area = 0
        while l<r:
            length = r-l
            breadth = min(height[l], height[r])
            max_area = max(length*breadth, max_area)

            if height[l]<=height[r]:
                l+=1
            else:
                r-=1

        return max_area 
