def rotate_array(nums: list, k: int) -> list:
    n = len(nums)
    if n == 0:
        return nums
    k = k % n
    return nums[-k:] + nums[:-k]

# Example Usage
print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]