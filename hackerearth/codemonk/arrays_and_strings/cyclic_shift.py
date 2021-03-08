# returns list of all the values of cyclic shifts where the A is B, i.e. max
def find_max_shifts(size_of_binary_string, binary_string):
    max_shift = binary_string
    max_shifts = []
    for shift in range(size_of_binary_string):
        current_shift = binary_string[size_of_binary_string - shift:] + binary_string[:size_of_binary_string - shift]
        if current_shift > max_shift:
            max_shift = current_shift
    for shift in range(size_of_binary_string, 0, -1):
        current_shift = binary_string[size_of_binary_string - shift:] + binary_string[:size_of_binary_string - shift]
        if current_shift == max_shift:
            max_shifts.append(size_of_binary_string - shift)
    return max_shifts


for T in range(int(input())):
    N, K = map(int, input().split())
    A = input()
    M = find_max_shifts(N, A)
    # print(M)
    size_of_max_shifts = len(M)
    shift_index = (K % size_of_max_shifts) - 1
    print(M[shift_index] + (N * ((K - 1) // size_of_max_shifts)))

"""
========
INPUT:
4
5 2
10101
6 2
010101
6 15
010101
5 2
11010
========
OUTPUT:
9
3
29
5
========
EXPLANATION:
For the 1st test case, the value of B is (11010).
After performing 4 cyclic shifts the value represented by array A
becomes equal to B for the first time.
After performing additional 5 cyclic shifts the value represented by array A
becomes B for the second time. Hence, the answer is
4 + 5 = 9

For the 2nd test case, the value of B is (101010).
After performing 1 cyclic shifts the value represented by array A
becomes equal to B for the first time.
After performing additional 2 cyclic shifts the value represented by array A
becomes B for the second time. Hence, the answer is
1 + 2 = 3
"""

"""
To check cyclic shifts accuracy
2
5 2
12345
6 2
123456
"""
