class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
        # Calculate the middle index using integer division
            mid = (left + right) // 2
        
            # Check if target is present at mid
            if nums[mid] == target:
                return mid
        
            # If target is greater, ignore left half
            elif nums[mid] < target:
                left = mid + 1
            
            # If target is smaller, ignore right half
            else:
                right = mid - 1
            
        # Target was not present in the list
        return -1