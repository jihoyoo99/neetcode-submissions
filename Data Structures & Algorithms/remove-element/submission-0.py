class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        copy = nums.copy()
        counter = 0
        for num in copy:
            if not num == val:
                nums[counter] = num 
                counter += 1
        return counter

