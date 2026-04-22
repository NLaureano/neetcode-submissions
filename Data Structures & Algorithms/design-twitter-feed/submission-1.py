class Twitter:

    def __init__(self):
        self.tweetFeed = [] # Stack
        self.users = {} # {int : {int}}

    def userCheck (self, userId: int) -> None:
        if userId not in self.users: self.users[userId] = set() # ensure exists

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userCheck(userId)
        self.tweetFeed.append((userId, tweetId)) # Add tweet to stack

    def getNewsFeed(self, userId: int) -> List[int]:
        self.userCheck(userId)        #
        follows = self.users[userId]  # Get followers
        follows.add(userId)
        stack = self.tweetFeed.copy() # Copy stack
        feed = []
        while stack and len(feed) < 10:
            uID, tID = stack.pop()
            if uID in follows:
                feed.append(tID)
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userCheck(followerId)
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userCheck(followerId)
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)

        
