# Number of subset having some specific sum
print("----------INPUT----------")

str_arr = input('Enter array of integers: ').split(' ')
arr = [int(num) for num in str_arr]

toEqual = int(input('Enter a sum: '))

# print("----------DP----------")

def add(arr, ind, sum, mem, toEqual):
    key = str(sum) + ':' + str(ind)
    if key in mem:
        return mem[key]
    if sum == toEqual:
        return 1
    if ind < 0:
        return 0
    to_return = add(arr, ind - 1, sum + arr[ind], mem, toEqual) + add(arr, ind - 1, sum, mem, toEqual)
    mem[key] = to_return
    return to_return

def toSum(arr, toEqual):
    mem = {}
    return add(arr, len(arr) - 1, 0, mem, toEqual)

print("----------OUTPUT----------")

result = toSum(arr, toEqual)
print(result)

print("----------END----------")
