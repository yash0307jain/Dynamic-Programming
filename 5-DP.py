# Longest Common Subsequence
print("----------INPUT----------")

# For arrays
# str_arr = input('Enter array of integers: ').split(' ')
# arr = [int(num) for num in str_arr]

# For strings
arr1 = input('Enter first array of strings: ')
arr2 = input('Enter second array of strings: ')

# print("----------DP----------")

def lcs(arr1, arr2, arr1Len, arr2len):
    if(arr1Len == 0 or arr2len == 0):
        return 0
    elif arr1[arr1Len - 1] == arr2[arr2len - 1]:
        return 1 + lcs(arr1, arr1, arr1Len - 1, arr2len - 1)
    else:
        return max(lcs(arr1, arr2, arr1Len - 1, arr2len), lcs(arr1, arr2, arr1Len, arr2len - 1))


print("----------OUTPUT----------")

print('Length Of Longest Common Subsequence: ', lcs(arr1, arr2, len(arr1), len(arr2)))

print("----------END----------")
