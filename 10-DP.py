#Maximum subarray without taking any adjacent elements
def toSum(arr, ind, mem, sum):
    if ind < 0:
        return mem

    mem.append(sum + arr[ind])
    # print(sum + arr[ind])
    
    toSum(arr, ind - 2, mem, sum + arr[ind])
    toSum(arr, ind - 1, mem, sum)

def splitSum(arr):
    mem = []
    toSum(arr, len(arr) - 1, mem, 0)
    return max(mem)

def maxSubsetSum(arr):
    maxSum = splitSum(arr)
    print(maxSum)
    # return maxSum

arr = list(map(int, input().split()))
maxSubsetSum(arr)
    