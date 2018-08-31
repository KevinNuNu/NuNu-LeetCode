class UnionFind:
    def __init__(self, n, data):
        self.n = n
        self.data = data
        # 初始化节点i的直接父节点parent[i]为自身i
        self.parent = list(range(n))
        # 初始化节点i作为根节点的树的高度为1
        self.rank = [1] * n

    def find(self, x):
        # 查询节点x的根节点
        r = x
        while r != self.parent[r]:
            r = self.parent[r]
        # 进行路径压缩
        i = x
        while self.parent[i] != r:
            self.parent[i], i = r, self.parent[i]
        return r

    def union(self, i, j):
        i_root = self.find(i)
        j_root = self.find(j)
        # 将高度较小的树连接到高度较大的树上
        if i_root != j_root:
            if self.rank[i_root] == self.rank[j_root]:
                self.parent[i_root] = j_root
                self.rank[j_root] += 1
            elif self.rank[i_root] > self.rank[j_root]:
                self.parent[j_root] = i_root
            else:
                self.parent[i_root] = j_root

    def solver(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.data[i][j] == 1:
                    self.union(i, j)
        s = 0
        for i in range(self.n):
            if self.parent[i] == i:
                s += 1
        return s


class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        uf = UnionFind(n, M)
        return uf.solver()

