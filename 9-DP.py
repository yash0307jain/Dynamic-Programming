# Game of two stacks
print("----------INPUT----------")

n = int(input())
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

# print("----------DP----------")

def splitSum(n, a, b, ind_a, ind_b, sum, ans, mem):
    key = str(ind_a) + ':' + str(ind_b)
    if key in mem:
        return mem[key]
    if sum >= n:
        # print('sum --> ', sum, ', ind_a --> ', ind_a, ', ind_b --> ', ind_b)
        if sum == n:
            ans.append(ind_a + ind_b)
        else:
            return ans.append(ind_a + ind_b - 1)
        
    # print('running')

    mem[key] = sum
    if ind_a < len(a):
        splitSum(n, a, b, ind_a + 1, ind_b, sum + a[ind_a], ans, mem)
    if ind_b < len(b):
        splitSum(n, a, b, ind_a, ind_b + 1, sum + b[ind_b], ans, mem)
    return ans

def toSplit(n, a, b):
    sum = 0
    mem = {}
    ans = []
    splitSum(n, a, b, 0, 0, sum, ans, mem)
    if len(ans) == 0:
        return len(a) + len(b)
    return max(ans)

print("----------OUTPUT----------")

print(toSplit(n, a, b))

print("----------END----------")
