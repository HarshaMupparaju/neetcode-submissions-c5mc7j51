class Twitter:

    def __init__(self):
        self.followers = {}
        self.time = 0
        self.tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if(userId not in self.tweets):
            self.tweets[userId] = set()
            self.followers[userId] = set()
        
        self.tweets[userId].add((-self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        max_hp = []

        users = set()
        users.add(userId)

        if(userId not in self.followers):
            return []

        for followeeId in self.followers[userId]:
            users.add(followeeId)
        
        #iterate over tweets
        for user in users:
            if user not in self.tweets:
                continue
            tweets = self.tweets[user]
            for tweet in tweets:
                heapq.heappush(max_hp, tweet)
        
        res = []

        while(len(res) < 10 and len(max_hp) > 0):
            t, tweetId = heapq.heappop(max_hp)
            res.append(tweetId)
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:

        if(followerId not in self.followers):
            self.followers[followerId] = set()


        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followerId not in self.followers):
            return
        
        if(followeeId not in self.followers[followerId]):
            return

        self.followers[followerId].remove(followeeId)