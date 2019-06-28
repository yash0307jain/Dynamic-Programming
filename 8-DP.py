# Rope Partition to get maximum multiplication value
print("----------INPUT----------")

num = int(input('Enter a number: '))

# print("----------DP----------")

def splitMul(num, mul, mem, memory):
    key = str(num) + ":" + str(mul)
    if key in memory:
        return memory[key]

    print("num --> ", num, " mul --> ", mul)

    if num < 2:
        if num > -1:
            return mem.append(mul)
        return mem
    
    memory[key] = mem
    splitMul(num - 2, mul * 2, mem, memory)
    splitMul(num - 3, mul * 3, mem, memory)

def maxMul(num):
    if num > 3:
        mul = 1
        mem = []
        memory = {}
        splitMul(num, mul, mem, memory)
        return max(mem)
    elif num < 4:
        return num - 1
    

print("----------OUTPUT----------")

print('Maximum multiplication: ', maxMul(num))

print("----------END----------")
