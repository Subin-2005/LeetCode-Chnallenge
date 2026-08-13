def merged(nums1, m, nums2, n):

    num1 = nums1[:m]

    result = num1 + nums2
    result.sort()

    for i in range(m + n):
        nums1[i] = result[i]
        return result

nums1 = [1,2,3,0,0,0]
nums2 = [2,3,5]
m = 3
n = 3
print(merged(nums1, m, nums2, n))