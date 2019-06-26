# Split into all the possible subset of an array can be either number of string
print("----------INPUT----------")

# For arrays
str_arr = input('Enter array of integers: ').split(' ')
arr = [int(num) for num in str_arr]

# For strings
# str_arr = input('Enter array of strings: ')
# arr = str_arr

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

result = toSplitList(arr)
print(result)

print("----------END----------")
