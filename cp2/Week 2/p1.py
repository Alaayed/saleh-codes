def recycle():
    n = int(input())
    bins =[]
    while len(bins) != n:
        bins.extend(list(map(int, input().split())))
    stack = []
    solution = (0 , 0 , -1)
    for i , b in enumerate(bins):
        popped = (0, i)
        while stack and stack[-1][0] >= b:
            popped = stack.pop()
            val, start, end= popped[0] , popped[1], i
            score = val * (end - start)
            if score >= solution[-1]:
                if score != solution[-1] or (score == solution[-1] and start < solution[0]):
                    solution = (start, end, score)
        stack.append( ( b , popped[1] ) )
    end = len(bins)
    while stack:
        popped = stack.pop()
        val, start = popped[0] , popped[1]
        score = val * (end - start)
        if score >= solution[-1]:
            if score != solution[-1] or (score == solution[-1] and start < solution[0]):
                solution = (start, end, score)
    print(f'{solution[0]+1} {solution[1]} {solution[2]}')
recycle()