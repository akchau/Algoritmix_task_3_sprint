"id = 73775272."


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
            if nums[0] > nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[0] < nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return -1
