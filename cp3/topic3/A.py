class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0 for i in range(n+1)]
    def _lsb(self, i):
        return i & -i
    def add(self, i , delta):
        while i <= self.n:
            self.bit[i]+= delta
            i += self._lsb(i)
    def sum(self, i):
        res = 0
        while i > 0:
            res+= self.bit[i]
            i -= self._lsb(i)
        return res
    def range_query(self, l, r):
        return self.sum(r)-self.sum(l-1)
    
def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    # Create a fenwick tree
    tree = FenwickTree(100_000+5)
    # inversions array
    inversions = [0 for i in range(n)]
    for i,n in enumerate(reversed(nums)): 
        # for each number, find how many are smaller
        inversions[i] = tree.sum(n-1)
        tree.add(n, 1)
    
    inversions.reverse()
    for i in range(len(inversions)):
        if inversions[i] == 0:
            inversions[i]= 1
    print(sum(inversions))




def calc_distance(i,j, tree: FenwickTree, n):
    if i > j:
        to_end = n-i - tree.range_query(i+1,n)
        
        from_start = j - tree.sum(j)-1
        total_distance = to_end + from_start
        print('i,j: ', i,j ," to end from start ", to_end, from_start, n)
    else:
        total_distance = j- i - tree.range_query(i+1, j) - 1
    return total_distance
def solve2():
    n = int(input())
    nums = list(map(int, input().split()))
    distances = []
    for i,n in enumerate(nums):
        distances.append([n,i+1])
    n= len(nums)
    distances.sort(reverse=True)
    prev = 0
    res = 0
    tree = FenwickTree(100_005)
    print(distances)
    while distances:
        value, index = distances.pop()
        print('checks:', index,prev, value,res)
        res+=calc_distance(prev, index, tree, n) +1
        tree.add(index,1)
        prev = index
    print(res)

solve2()