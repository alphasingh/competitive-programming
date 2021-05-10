"""
https://www.codechef.com/APRIL21C/problems/BOLT
"""

from decimal import Decimal


def is_world_record_possible(factor1: float, factor2: float, factor3: float, speed: float) -> bool:
    final_speed = speed * factor1 * factor2 * factor3
    time_taken_for_100m = 100 / final_speed
    rounded_off = float(round(Decimal(time_taken_for_100m), 2))
    return rounded_off < 9.58  # strictly less than world record


assert is_world_record_possible(1.0, 1.0, 1.0, 10) is False
assert is_world_record_possible(1.0, 1.0, 1.0, 10.45) is True
"""
TestCase 1: Final speed of Chef after considering all the factors will be 1∗1∗1∗10.45=10.45 m / sec. 
So the time taken to complete the race will be 100/10.45=9.569=9.57 sec after rounding to 2 places after decimal. 
Since the time is strictly less than the world record time, therefore Chef can break the record.
"""
assert is_world_record_possible(1.0, 1.0, 1.0, 10.44) is False
"""
TestCase 2: Final speed of Chef after considering all the factors will be 1∗1∗1∗10.44=10.44 m / sec. 
So the time taken to complete the race will be 100/10.44=9.578=9.58 sec after rounding to 2 places after decimal. 
Since the time is equal to the world record time, therefore Chef can't break the record.
"""
assert is_world_record_possible(1.0, 1.0, 0.9, 10.44) is False
"""
TestCase 3: Final speed of Chef after considering all the factors will be 1∗1∗0.9∗10.44=9.396 m / sec. 
So the time taken to complete the race will be 100/9.396=10.643=10.64 sec after rounding to 2 places after decimal. 
Since the time is strictly more than the world record time, therefore Chef can't break the record.
"""

for T in range(int(input())):
    k1, k2, k3, v = map(float, input().split())
    if is_world_record_possible(k1, k2, k3, v):
        print('YES')
    else:
        print('NO')
