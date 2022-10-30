def broken_search(nums, target) -> int:
    right = len(nums)
    left = 0
    first = nums[0]
    mid = (right + left) // 2
    if first == target:
        return 0
    while right - left >= 2:
        if first > target:
            if nums[mid] == target:
                return mid
            if nums[mid] > target and nums[mid] < nums[0]:
                right = mid
            else:
                left = mid
            mid = (right + left) // 2
        else:
            if first < target:
                if nums[mid] == target:
                    return mid
            if nums[mid] < target and nums[mid] > nums[0]:
                left = mid
            else:
                right = mid
            mid = (right + left) // 2
    return -1