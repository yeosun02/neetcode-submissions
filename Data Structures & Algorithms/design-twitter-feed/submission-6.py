class Twitter:

    def __init__(self):
        self.followers = {}
        self.user_posts = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_posts:
            self.user_posts[userId] = []
        
        self.user_posts[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        hp = []
        users = {userId}
        if userId in self.followers:
            users |= self.followers[userId]
        
        for user in users:
            if user in self.user_posts:
                idx = len(self.user_posts[user]) - 1
                count, tweetId = self.user_posts[user][idx]
                heapq.heappush(hp, (count, tweetId, user, idx - 1))

        res = []
        while hp and len(res) < 10:
            _, tweetId, user, idx = heapq.heappop(hp)
            res.append(tweetId)

            if idx != -1:
                count, tweetId = self.user_posts[user][idx]
                heapq.heappush(hp, (count, tweetId, user, idx - 1))
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)