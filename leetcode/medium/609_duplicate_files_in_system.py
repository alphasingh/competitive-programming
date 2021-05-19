"""
https://leetcode.com/problems/find-duplicate-file-in-system/
"""


class Solution:

    @staticmethod
    def findDuplicate(paths: [str]) -> [[str]]:
        files = dict()  # values contain all the files that have the key as content
        duplicate_files = []
        for path in paths:
            files_in_path = path.split()
            directory = files_in_path[0]
            for file in files_in_path[1:]:  # exclude the directory
                file_name_and_content = file.split('(')
                file_content = file_name_and_content[-1][:-1]
                # print(file_content)
                files.setdefault(file_content, [])
                files[file_content].append(directory + '/' + file_name_and_content[0])
        # print(files)
        for content in files:
            if len(files[content]) > 1:
                duplicate_files.append(files[content])
        return duplicate_files


sol = Solution()
assert sol.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)",
                          "root/c 3.txt(abcd)",
                          "root/c/d 4.txt(efgh)",
                          "root 4.txt(efgh)"]) == [["root/a/1.txt", "root/c/3.txt"],
                                                   ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"]]
assert sol.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)",
                          "root/c 3.txt(abcd)",
                          "root/c/d 4.txt(efgh)"]) == [["root/a/1.txt", "root/c/3.txt"],
                                                       ["root/a/2.txt", "root/c/d/4.txt"]]
assert sol.findDuplicate(["root/a 1.txt(xyz) 2.txt(efgh)",
                          "root/c 3.txt(abcd)",
                          "root/c/d 4.txt(efgh)",
                          "root 4.txt(efgh)"]) == [["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"]]
