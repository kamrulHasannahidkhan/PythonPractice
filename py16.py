def two_sum(nums: list, target: int) -> list:
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return []

# Example Usage
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]