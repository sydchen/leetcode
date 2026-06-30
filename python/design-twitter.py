'''
Design Twitter

需求：
- postTweet(userId, tweetId)：使用者發 tweet
- getNewsFeed(userId)：回傳自己和 followees 的最新 10 則 tweet id
- follow(followerId, followeeId)：追蹤
- unfollow(followerId, followeeId)：取消追蹤

核心想法：
每個 user 的 tweet 按照發文時間 append 到自己的 list。
查詢 news feed 時，只需要從「自己 + followees」這些來源中取最新 10 則。

解法：Hash Map + Heap
1. tweets[userId] 存這個 user 發過的 tweets，格式是 (time, tweetId)
2. follows[followerId] 存這個 user 追蹤了哪些 followee
3. getNewsFeed 時：
   - 對每個來源 user，先把該 user 最新 tweet 放進 max heap
   - 每 pop 出一則 tweet，就把同一 user 的前一則 tweet 放進 heap
   - 最多取 10 則

為什麼可行：
每個 user 的 tweet list 已經按時間由舊到新排列。
用 heap 可以在多個來源中，每次取出目前最新的一則。

時間複雜度：
- postTweet: O(1)
- follow / unfollow: O(1) average
- getNewsFeed: O((f + 10) log f)，f = 自己 + followees 的來源數

空間複雜度：O(T + F)，T = tweet 總數，F = follow 關係數
'''

import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        heap = []
        feed = []
        users = self.follows[userId] | {userId}

        for uid in users:
            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweet_id = self.tweets[uid][index]
                # heapq 是 min heap；用負 time 讓最新 tweet 先被 pop。
                heapq.heappush(heap, (-time, tweet_id, uid, index))

        while heap and len(feed) < 10:
            _, tweet_id, uid, index = heapq.heappop(heap)
            feed.append(tweet_id)

            prev_index = index - 1
            if prev_index >= 0:
                time, prev_tweet_id = self.tweets[uid][prev_index]
                heapq.heappush(heap, (-time, prev_tweet_id, uid, prev_index))

        return feed

    def follow(self, followerId, followeeId):
        if followerId == followeeId:
            return

        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.follows[followerId].discard(followeeId)


twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))
