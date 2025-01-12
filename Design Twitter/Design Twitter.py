import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0
        self.followers = defaultdict(list)  # follow map: user->[followers]
        self.userTweetMap = defaultdict(list)  # user-tweet map: user->[[time, tweetID]]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.userTweetMap[userId].append([self.time, tweetId])

        if userId not in self.followers:
            self.followers[userId] = [userId]

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followers:
            return []

        followers = self.followers[userId]
        tweets = []
        for follower in followers:
            if follower not in self.userTweetMap:
                continue
            tweets.extend(self.userTweetMap[follower])
        heapq.heapify(tweets)

        feed = []
        i = 0
        length = len(tweets)
        while i < 10 and i < length:
            feed.append(heapq.heappop(tweets)[1])
            i+=1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)
        if followerId not in self.followers:
            self.followers[followerId] =[followerId, followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
param_2 = obj.getNewsFeed(1)
obj.follow(1, 2)
obj.unfollow(1, 2)