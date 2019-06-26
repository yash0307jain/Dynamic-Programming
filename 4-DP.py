# Longest Common Subsequence
print("----------INPUT----------")

# For arrays
# str_arr = input('Enter array of integers: ').split(' ')
# arr = [int(num) for num in str_arr]

# For strings
arr1 = input('Enter first array of strings: ')
arr2 = input('Enter second array of strings: ')

# print("----------DP----------")

def splitList(arr, ind, mem, all_mem):
    if ind < 0:
        return all_mem.append(mem)
    temp = mem.copy()
    mem.append(arr[ind])
    splitList(arr, ind - 1, mem, all_mem)
    splitList(arr, ind - 1, temp, all_mem)

def toSplitList(arr):
    mem = []
    all_mem = []
    splitList(arr, len(arr) - 1, mem, all_mem)
    return all_mem

print("----------OUTPUT----------")

result1 = toSplitList(arr1)
result2 = toSplitList(arr2)

maxLength = 0

for str1 in result1:
    for str2 in result2:
        if(str1 == str2):
            leng = len(str1)
            if(maxLength < leng):
                maxLength = leng

print('Length Of Longest Common Subsequence: ', maxLength)

print("----------END----------")
