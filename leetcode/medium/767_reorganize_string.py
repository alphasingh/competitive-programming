"""
https://leetcode.com/problems/reorganize-string/
"""

import heapq


class Solution:
    @staticmethod
    def reorganizeString(s: str) -> str:
        heap = {}
        used = (0, '')  # count, char
        for char in s:
            if char not in heap:
                heap[char] = 0
            heap[char] += 1
        # print(heap)
        heap = [(-v, k) for k, v in heap.items()]
        # print(heap)
        heapq.heapify(heap)
        r = []
        while heap:
            v, k = heapq.heappop(heap)
            # print('popped ', (v,k), 'used ', used)
            if k == used[1]:  # not possible
                r = []
                break
            if used[0] != 0:
                heapq.heappush(heap, used)
            used = (v + 1, k)
            r.append(k)
        return ''.join(r) if used[0] == 0 else ''


assert Solution.reorganizeString("aab") == "aba"
assert Solution.reorganizeString("aaab") == ""
"""
"aaaabbbc"
"aaabbbc"
"a"
"abc"
"aab"
"aaab"
"""
