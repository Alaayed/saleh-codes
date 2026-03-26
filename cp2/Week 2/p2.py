def dommy_duos():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    res = 0
    stack = []
    for i in range(n):
        while stack and stack[-1] <= nums[i]:
            e = stack.pop()
            res += 1 + min(1, len(stack))
        stack.append(nums[i])
    res += max(0, len(stack) - 1)
    return res
print(dommy_duos())
