import time

print("----------INPUT----------")

n = int(input('Enter a number--> '))

print("----------WITH DP----------")

def sumDP(num, mem):
    if num in mem:
        return mem[num]
    if num <= 0:
        return num
    print(num)
    to_return = sumDP(num-1, mem) + sumDP(num-2, mem)
    mem[num] = to_return
    return to_return

mem = {}
start1 = time.time()
result1 = sumDP(n, mem)
end1 = time.time()

print("----------WITHOUT DP----------")

def sum(num):
    if num <= 0:
        return num
    print(num)
    return sum(num-1) + sum(num-2)

start2 = time.time()
result2 = sum(n)
end2 = time.time()

print("----------OUTPUT----------")

print("Result 1 with DP --> ", result1)
print("Time 1 --> ", end1 - start1)
print("Result 2 without DP --> ", result2)
print("Time 2 --> ", end2 - start2)

print("----------END----------")
