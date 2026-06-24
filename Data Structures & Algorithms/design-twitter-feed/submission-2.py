class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.users = {}
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.t, tweetId))
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        all_tweets = [tweet for tweet in self.tweets[userId]]
        if userId in self.users:
            for friend in self.users[userId]:
                all_tweets += self.tweets.get(friend, [])
            all_tweets.sort()
        num = len(all_tweets)
        for i in range(num - 1, max(-1, num - 11), -1):
            res.append(all_tweets[i][1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.users:
            self.users[followerId] = set()
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)