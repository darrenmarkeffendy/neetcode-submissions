class Solution:
    def maxArea(self, heights: List[int]) -> int:
        return_set = set()
        lp, rp = 0, len(heights) - 1
        while lp < rp:
            return_set.add(min(heights[rp], heights[lp]) * (rp - lp))
            if heights[lp] <= heights[rp]:
                lp += 1
            elif heights[lp] > heights[rp]:
                rp -=1
        return max(return_set)