"""
https://leetcode.com/problems/simplify-path/
"""


class Solution:
    @staticmethod
    def simplifyPath(path: str) -> str:
        stack = []
        path = path.split('/')
        # print(path)
        for token in path:
            if token == '..':
                if stack and stack[-1]:
                    stack.pop()
            elif token == '.' or token == '':
                pass
            else:
                stack.append(token)
        # print(stack)
        canonical = '/' + '/'.join(stack).rstrip('/') if stack else '/'
        # print(canonical)
        return canonical


assert Solution.simplifyPath(path="/home/") == "/home"
"""
Explanation: Note that there is no trailing slash after the last directory name.
"""
assert Solution.simplifyPath(path="/../") == "/"
"""
Explanation: Going one level up from the root directory is a no-op, 
as the root level is the highest level you can go.
"""
assert Solution.simplifyPath(path="/home//foo/") == "/home/foo"
"""
Explanation: In the canonical path, 
multiple consecutive slashes are replaced by a single one.
"""
assert Solution.simplifyPath(path="/home//foo/../...") == "/home/..."
"""
Explanation: 
/home->/home/foo->/home->/home/...
since .. means parent folder and ... means a folder name
"""
