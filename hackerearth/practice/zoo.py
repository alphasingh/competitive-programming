def solve(word: str) -> bool:
    o = word.count('o')  # can be done in one pass
    return o == 2 * (len(word) - o)


assert solve("zoo") is True
assert solve("zo") is False
assert solve("zoozoo") is True
