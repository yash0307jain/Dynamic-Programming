# Calculation of time difference between code with DP and without DP
import time

print("----------INPUT----------")

n = int(input('Enter a number--> '))

print("----------WITH DP----------")

def splittingDP(num, mem):
    if num in mem:
        return mem[num]
    if num <= 1:
        print(num)
        return num
    # print(num)
    to_return = splittingDP(num-1, mem) + splittingDP(num-2, mem)
    mem[num] = to_return
    return to_return

mem = {}
start1 = time.time()
result1 = splittingDP(n, mem)
end1 = time.time()

print("----------WITHOUT DP----------")

def splitting(num):
    if num <= 1:
        print(num)
        return num
    # print(num)
    return splitting(num-1) + splitting(num-2)

start2 = time.time()
result2 = splitting(n)
end2 = time.time()

print("----------OUTPUT----------")

print("Result 1 with DP --> ", result1)
print("Time 1 --> ", end1 - start1)
print("Result 2 without DP --> ", result2)
print("Time 2 --> ", end2 - start2)

print("----------END----------")
