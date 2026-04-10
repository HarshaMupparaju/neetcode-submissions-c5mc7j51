class Twitter:

    def __init__(self):
        self.follow_dict = {} # This is a dict of dict, with key as followerId and value is a dict of followeeIds
        self.tweets_dict = {} # {userId: [tweet_id1, tweet_id2]}
        self.tweet_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if(userId in self.tweets_dict):
            self.tweets_dict[userId].append([self.tweet_count, tweetId])
        else:
            self.tweets_dict[userId] = [[self.tweet_count, tweetId]]
        
        self.tweet_count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #Get atmost 10 tweets ordered from most recent to least recent that are posted by the user or from the people the user follows
        res = []

        #Get all relevant users
        all_relevant_users = []
        all_relevant_users.append(userId)

        if(userId in self.follow_dict):
            d = self.follow_dict[userId]

            for k in d:
                all_relevant_users.append(k)
        
        hp = []

        for user in all_relevant_users:
            if(user in self.tweets_dict):
                tweet = self.tweets_dict[user][-1]
                heapq.heappush(hp, [tweet[0], tweet[1], user, -1])
        
        while(len(hp) != 0):

            top = heapq.heappop(hp)

            tweet_id = top[1]
            user_id = top[2]
            index = top[3]

            res.append(tweet_id)

            if(-1 * (index - 1) <= len(self.tweets_dict[user_id])):
                tweet = self.tweets_dict[user_id][index - 1]
                heapq.heappush(hp, [tweet[0], tweet[1], user_id, index - 1])

            if(len(res) == 10):
                break

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if(followerId == followeeId):
            return

        if(followerId in self.follow_dict):
            self.follow_dict[followerId][followeeId] = 1
        else:
            self.follow_dict[followerId] = {followeeId : 1}
        
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followerId == followeeId):
            return

        if(followerId in self.follow_dict):
            if(followeeId in self.follow_dict[followerId]):
                del self.follow_dict[followerId][followeeId]
        
        return
