import tweepy
import geocoder

class Twitter():
        """
        There is a rate limit for usage therefore you have to manually adjust the application to
        get the desired results.
        possible operations from the tweeter API:

        Premium search
        Get Tweets(Authenticated User Timeline)
        Post, Retrieve and other Engagements with tweets
        Search Tweets
        Create and Mange Tweets
        Follow search and Get users
        Manage Account Settings
        Mute block
        Sending and Recieving Messages
        Upload media
        Get location with trendig tweets
        Geo information
        And more customise Usage
        """
        def __init__(self):
            pass

        def Authentication(self):
            
            """
            these tokens and api keys have to be created maunally from the twiter developers page            """

            accessToken = "902085364537536512-J28kNYKcf8EM5XTGELxqIsYOVRR2NtE"
            accessTokenSecret = "dv51Hsxrmqv3PHZGeBkT6tCcI5xNUZ7ktw5GgGC4J7AMi"
            bearerToken = "AAAAAAAAAAAAAAAAAAAAAPzd%2BwAAAAAAcicemBiLypPZ1PPWT%2BottGjh4So%3Dhhlf1OS7LgUZb9jPYk7PuK5nn1SopU0bvbZGptjpDYJ9da4Qaj"
            consumerApiKey = "8qfhyu0vWmMUJ1cccx2ArRE4w"
            consumerApiSecretKey = "0JIVYC59t16Ux2z7v2BD9qIBLJijTiu4IJKQV5VLQRH1qPza0y"

            auth = tweepy.OAuthHandler(consumerApiKey, consumerApiSecretKey)
            auth.set_access_token(accessToken, accessTokenSecret)
            api = tweepy.API(auth)
            return api
       
        def Tweets(self, api):
            screenName = "@sidney_sanday"
            tweets = api.home_timeline(count=7, tweet_mode="extended")
            tweetList = []
            for tweet in tweets:
                text = tweet.full_text.replace('\n\n','\n' )
                tweetList.append("\n\n{}\n\n*".format(text))
            return tweetList

        def UserDetails(self,api,  userName):
            user = api.get_user(screen_name=userName)
            userName = user.screen_name
            followersCount = user.followers_count
            followersList = []
            for friend in user.friends():
                followersList.append(friend.screen_name)
            return(userName, followersCount, followersList)

        def Search():
            pass
        
        def Trending(self, api):
            geo = geocoder.osm("kenya")
            trendingTopics = api.closest_trends(geo.lat, geo.lng)
            trends =  api.get_place_trends(trendingTopics[0]["woeid"])
            print(trends)
            return trends
            
        def RetrieveUserData():
            pass

        def DirectMessages():
            pass

def main():
    twitter = Twitter()

if __name__ == "__main__":
    main()
