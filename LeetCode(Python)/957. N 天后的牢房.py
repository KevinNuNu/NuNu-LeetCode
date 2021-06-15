import copy

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def next_day_cells(cells):
            return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1]) for i in range(8)]

        seen = {}
        find_same = False

        for i in range(1, n+1):
            cells = next_day_cells(cells)
            c = tuple(cells)
            if not seen.get(c, None):
                seen[c] = i
            else:
                find_same = True
                last_idx = seen.get(c)
                iter_num = i - last_idx
                break

        reverse_seen = {}
        for k,v in seen.items():
            reverse_seen[v] = k

        if find_same:
            target = (n - last_idx) % iter_num + last_idx
            return reverse_seen[target]
        else:
            return reverse_seen[n]