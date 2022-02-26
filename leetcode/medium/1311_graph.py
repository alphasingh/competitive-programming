"""
https://leetcode.com/contest/weekly-contest-170/problems/get-watched-videos-by-your-friends/
"""

from collections import Counter


class Solution:
    @staticmethod
    def watched_videos_by_friends(watched_videos: [[str]], friends: [[int]], _id: int, level: int) -> [str]:
        n = len(friends)
        INF = 10 ** 10

        dist = [[INF] * n for _ in range(n)]

        # add given distance between edges
        for i in range(n):
            dist[i][i] = 0
            for friend in friends[i]:
                dist[friend][i] = 1
                dist[i][friend] = 1

        # Floyd-Warshall to calculate shortest distances from one friend to another
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    dist[i][k] = min(dist[i][k], dist[i][j] + dist[j][k])

        friends_at_level = []
        for friend in range(n):
            if dist[_id][friend] == level:
                friends_at_level.append(friend)

        print('friends_at_level', friends_at_level)
        # print(depths)

        videos_watched_by_level_friends = []
        for friend in friends_at_level:
            videos_watched_by_level_friends += watched_videos[friend]
        # print('videos_watched_by_level_friends', videos_watched_by_level_friends)

        video_counter = Counter(videos_watched_by_level_friends)
        # print('video_counter', video_counter)
        videos_at_level = []
        for v, c in video_counter.items():
            videos_at_level.append((v, c))

        # sort by frequency, then alphabetically
        videos_at_level.sort(key=lambda x: (x[1], x[0]))

        return [video for video, frequency in videos_at_level]


assert Solution.watched_videos_by_friends(watched_videos=[["A", "B"], ["C"], ["B", "C"], ["D"]],
                                          friends=[[1, 2], [0, 3], [0, 3], [1, 2]],
                                          _id=0,
                                          level=1) == ["B", "C"]
"""
Explanation: 
You have id = 0 (green color in the figure) and your friends are (yellow color in the figure):
Person with id = 1 -> watchedVideos = ["C"] 
Person with id = 2 -> watchedVideos = ["B","C"] 
The frequencies of watchedVideos by your friends are: 
B -> 1 
C -> 2
"""
assert Solution.watched_videos_by_friends(watched_videos=[["A", "B"], ["C"], ["B", "C"], ["D"]],
                                          friends=[[1, 2], [0, 3], [0, 3], [1, 2]],
                                          _id=0,
                                          level=2) == ["D"]
"""
You have id = 0 (green color in the figure) 
and the only friend of your friends is the person with id = 3 (yellow color in the figure).
"""
