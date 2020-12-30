import sys
class djs:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1 for i in range(n + 1)]
    def find(self, u):
        if u==self.parent[u]:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a==b:
            return
        if self.rank[a] > self.rank[b]:
            a, b = b, a
        self.parent[a] = b
        if self.rank[a] == self.rank[b]:
            self.rank[b] += 1
if __name__ == "__main__":
    N, Q = map(int, sys.stdin.readline().split())
    g = [i for i in range(N+1)]
    ds = djs(N)
    s = []
    query = []
    for i in range(2, N+1):
        g[i] = int(sys.stdin.readline())
    for i in range(N+Q-1):
        query.append(map(int, sys.stdin.readline().split()).__iter__())
    for i in range(N+Q-2, -1, -1):
        a = query[i]
        b = next(a)
        if b==0:
            temp = next(a)
            ds.union(temp, g[temp])
        else:
            c, d = next(a), next(a)
            if ds.find(c) == ds.find(d):
                s.append(True)
            else:
                s.append(False)
    while len(s)!=0:
        if s.pop():
            print("YES")
        else:
            print("NO")