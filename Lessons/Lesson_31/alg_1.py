def search_range(nums, target):
    def binary_search(nums, target, find_first):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                result = mid

                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    left_pos = binary_search(nums, target, find_first=True)
    right_pos = binary_search(nums, target, find_first=False)

    return [left_pos, right_pos]


sorted_array = [1, 2, 2, 3, 4, 4, 4, 5, 6]
target_element = 1

result = search_range(sorted_array, target_element)
print(result)
