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
        
        user_post_idx = {}
        for user in users:
            if user in self.user_posts:
                heapq.heappush(hp, (self.user_posts[user][-1][0], user))
                user_post_idx[user] = len(self.user_posts[user]) - 1

        res = []
        while hp and len(res) < 10:
            _, user = heapq.heappop(hp)
            res.append(self.user_posts[user][user_post_idx[user]][1])

            if user_post_idx[user] != 0:
                user_post_idx[user] -= 1
                heapq.heappush(hp, (self.user_posts[user][user_post_idx[user]][0], user))
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)