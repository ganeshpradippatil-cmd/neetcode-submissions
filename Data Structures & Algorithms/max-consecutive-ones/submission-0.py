class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        max_val = 0
        for num in nums:
            if num == 1:
                current_streak += 1
            else:
                # Update   max_val and reset streak
                max_val = max(max_val, current_streak)
                current_streak = 0
        return max(max_val, current_streak)