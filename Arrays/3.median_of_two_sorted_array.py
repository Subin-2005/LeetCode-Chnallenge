def findMedianSortedArrays(nums1, nums2):
    arr = nums1 + nums2

    arr.sort()

    n = len(arr)

    mid = n // 2

    if n % 2 == 1:
        return float(arr[mid])
    else:
        return (arr[mid - 1] + arr[mid]) / 2

nums1 = [1,2,3]
nums2 = [4,5]

result = findMedianSortedArrays(nums1, nums2)
print(result)