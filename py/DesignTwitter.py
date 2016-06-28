import collections

class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followship = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)
        self.cnt = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets[userId].append([tweetId, self.cnt])
        self.cnt += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        userlist = list(self.followship[userId]) + [userId]
        user_tweet_index = [[userId, len(self.tweets[userId])-1] for userId in userlist if userId in self.tweets]
        retlist = []

        for _ in xrange(10):
            max_index = max_tweet_id = max_user_id = -1
            for i, (user_id, tweet_index) in enumerate(user_tweet_index):
                if tweet_index >= 0:
                    tweet_info = self.tweets[user_id][tweet_index]
                    if tweet_info[1] > max_tweet_id:
                        max_index, max_user_id, max_tweet_id = i, user_id, tweet_info[1]
            if max_index == -1:
                break

            retlist.append(self.tweets[max_user_id][user_tweet_index[max_index][1]][0])
            user_tweet_index[max_index][1] -= 1
        return retlist

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId == followerId: return
        self.followship[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followship and followeeId in self.followship[followerId]:
            self.followship[followerId].remove(followeeId)
