class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        max_streak = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_streak += 1
            if nums[i] == 0:
                if current_streak > max_streak:
                    max_streak = current_streak
                current_streak = 0 
            if i == len(nums) - 1 and nums[i] == 1:
                if current_streak > max_streak:
                    max_streak = current_streak
        return max_streak


print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))