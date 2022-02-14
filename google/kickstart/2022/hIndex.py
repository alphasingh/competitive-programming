def h_index(n: int, citations: [int]):
    ans = list()
    h_so_far = 0
    for i in range(n):
        count = 0
        for j in range(i + 1):
            if citations[j] > h_so_far:
                count += 1
        if count == h_so_far + 1:
            h_so_far += 1
        ans.append(h_so_far)

    return ans


assert h_index(3, [5, 1, 2]) == [1, 1, 2]
assert h_index(6, [1, 3, 3, 2, 2, 15]) == [1, 1, 2, 2, 2, 3]
assert h_index(6, [1, 1, 4, 4, 4, 4]) == [1, 1, 1, 2, 3, 4]

if __name__ == '__main__':
    t = int(input())

    for test_case in range(1, t + 1):
        N = int(input())  # The number of papers
        C = list(map(int, input().split()))  # The number of citations for each paper
        h_index_scores = h_index(N, C)
        print("Case #" + str(test_case) + ": " + ' '.join(map(str, h_index_scores)))

"""
2
3
5 1 2
6
1 3 3 2 2 15
"""
"""
Case #1: 1 1 2
Case #2: 1 1 2 2 2 3
"""
