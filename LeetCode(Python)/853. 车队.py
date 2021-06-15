import copy


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        num = len(position)
        if not num:
            return 0

        dist_time = []
        for pos, s in zip(position, speed):
            dist = target - pos
            arrive_time = dist / s
            dist_time.append([dist, arrive_time])
        sorted_dist_time = sorted(dist_time, key=lambda x: x[0])
        # print(sorted_dist_time)

        for i in range(num - 1):
            t1 = sorted_dist_time[i][1]
            t2 = sorted_dist_time[i+1][1]
            if t1 >= t2:
                sorted_dist_time[i+1][1] = sorted_dist_time[i][1]
        # print(sorted_dist_time)

        return len(set([item[1] for item in sorted_dist_time]))