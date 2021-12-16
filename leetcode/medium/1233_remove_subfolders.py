"""
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
"""


class Solution:
    @staticmethod
    def removeSubfolders(folder: [str]) -> [str]:
        folder.sort()
        parents = {folder[0]}
        current = folder[0] + '/'
        for f in folder:
            if current != f[:len(current)]:
                parents.add(f)
                current = f + '/'
        return parents


assert set(Solution.removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])) == {"/a", "/c/d", "/c/f"}
# Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
assert set(Solution.removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"])) == {"/a"}
# Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".
assert set(Solution.removeSubfolders(folder=["/a/b/c", "/a/b/ca", "/a/b/d"])) == {"/a/b/c", "/a/b/ca", "/a/b/d"}
