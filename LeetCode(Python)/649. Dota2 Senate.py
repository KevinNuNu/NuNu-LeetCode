class Solution:
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        from collections import deque
        n = len(senate)
        q_r, q_d = deque(), deque()
        for i in range(n):
            if senate[i] == 'R':
                q_r.append(i)
            else:
                q_d.append(i)

        # 巧妙之处：利用贪心算法，每一个参议员ban掉其后面最近的对方参议员
        # 每次比较两个队列的头元素，并且用"+n"的方法，将获胜的参议员重新放入比较队列参与下一轮ban人
        while q_r and q_d:
            r, d = q_r.popleft(), q_d.popleft()
            if r < d:
                q_r.append(r + n)
            else:
                q_d.append(d + n)

        return 'Radiant' if q_r else 'Dire'


if __name__ == '__main__':
    s = Solution()
    print(s.predictPartyVictory('DRRD'))
