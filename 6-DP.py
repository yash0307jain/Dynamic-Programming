# Minimum Partition
print("----------INPUT----------")

str_arr = input('Enter array of integers: ').split(' ')
arr = [int(num) for num in str_arr]

# print("----------DP----------")

def splitArr(arr, newArr, ind, mem):
    if ind < 0:
        sub = abs(sum(arr) - sum(newArr))
        if sub not in mem:
            mem[sub] = [arr, newArr]
        return mem

    oldArr = arr.copy()
    old_newArr = newArr.copy()
    newArr.append(arr[ind])
    del arr[ind]

    splitArr(arr, newArr, ind - 1, mem)
    splitArr(oldArr, old_newArr, ind - 1, mem)

def minPartition(arr):
    mem = {}
    newArr = []
    splitArr(arr, newArr, len(arr) - 1, mem)
    return mem

print("----------OUTPUT----------")

result = minPartition(arr)
minKey = min(result.keys())
print(result[minKey])

print("----------END----------")
