# Subset Subsequence
print("----------INPUT----------")

n, num = input().split(' ')
n = int(n)
num = int(num)
str_arr = input().split(' ')
test_arr = [int(number) for number in str_arr]

arr = []
for i in range(0,n):
    if test_arr[i] <= num:
        arr.append(test_arr[i])

# print("----------DP----------")

def ss(arr, num, ind, mem, count, memory):
    if mem > num:
        return count

    key = str(ind) + ":" + str(mem)
    
    if key in memory:
        count.append(1)
        return memory[key]
        
    print("ind --> ", ind, " mem --> ", mem)

    if ind < 0:
        memory[key] = mem
        return count.append(1)
    
    ss(arr, num, ind - 1, mem * arr[ind], count, memory)
    ss(arr, num, ind - 1, mem, count, memory)

def toSS(arr, num):
    mem = 1
    count = []
    memory = {}
    ss(arr, num, len(arr) - 1, mem, count, memory)
    return count

print("----------OUTPUT----------")

arr = sorted(arr, reverse = True)

result = toSS(arr, num)
print(len(result) - 1)

print("----------END----------")
