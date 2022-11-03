"id = 73653079."


def broken_search(nums, target) -> int:
    right = len(nums)-1
    left = 0
    first = nums[0]
    if first == target:
        return 0
    while right >= left:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        if first > target:
            if nums[mid] > target and nums[mid] < nums[0]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target and nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
