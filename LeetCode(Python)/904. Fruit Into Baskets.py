from collections import deque


class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        n = len(tree)

        if n == 1:
            return 1

        queue = deque()
        tag_first = 0
        tag_second = 0
        cur_length = 0
        max_length = 0

        for index, item in enumerate(tree):
            if index == 0:
                queue.append(tree[index])
                cur_length += 1
                max_length = max(cur_length, max_length)
                continue

            if len(queue) == 1:
                if item != queue[0]:
                    queue.append(item)
                    tag_second = index
                cur_length += 1
            else:
                if item == queue[0]:
                    queue.popleft()
                    queue.append(item)
                    tag_first, tag_second = tag_second, index
                    cur_length += 1
                elif item == queue[1]:
                    cur_length += 1
                else:
                    queue.popleft()
                    queue.append(item)
                    tag_first, tag_second = tag_second, index
                    cur_length = index - tag_first + 1
            max_length = max(cur_length, max_length)

        return max_length


if __name__ == '__main__':
    s = Solution()
    print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
