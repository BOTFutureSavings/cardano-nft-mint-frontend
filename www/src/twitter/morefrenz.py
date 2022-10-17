import tweepy

accessToken = "dwN8OxcdVSj2qFNhw2AUu5xcW"
accessTokenSecret = "Sxyob1TFFbPT8nxG8XGUb9iye5WmbvQLuoeG9ZszhCEFIkDBOu"
bearerToken = "AAAAAAAAAAAAAAAAAAAAAEm0hwEAAAAAi4u2F0iL7B9tKaxuLIR%2FyNndAtU%3Dm8FI0zTjIKbvAdO1m413vPAIRpPLKUOFeVn8sZ3DhSgLyWsbzb"
consumerKey = ""
consumerSecret = ""

CLIENT = tweepy.Client(bearer_token=bearerToken, access_token=accessToken, access_token_secret=accessTokenSecret)

prospectedFollowerDataMaps = []
alreadyFollowingDataMaps = []

def prospectFollowerDataMap(userId, userName, name):
    followerData = {
        "userId" : userId,
        "userName" : userName,
        "name" : name
    }
    return followerData

def getFollowers(targetTwitterAccount):
    print(f'Getting the list of followers for { targetTwitterAccount }')
    friends = []
    friendsScreenName = []
    user_data = CLIENT.get_user(username=targetTwitterAccount, expansions=None, tweet_fields=None, user_fields=None, user_auth=False)
    user_id = user_data[0]['id']
    followers = CLIENT.get_users_followers(user_id, expansions=None, max_results=5, pagination_token=None, tweet_fields=None, user_fields=None, user_auth=False)
    for i in followers.data:
        followerData = prospectFollowerDataMap(i.data['id'],i.data['username'],i.data['name'])
        prospectedFollowerDataMaps.append(followerData)
    for follower_name in followers.data:
        friends.append(follower_name)
        screenName = f'@{follower_name}'
        friendsScreenName.append(screenName)
    print(f'Fetched number of following for { targetTwitterAccount } : { len(friends) }')            
    return friends,friendsScreenName

def selfGetCurrentFollowing(selfAccount):
    # get following list from current authenticated account
    user_data = CLIENT.get_user(username=selfAccount, expansions=None, tweet_fields=None, user_fields=None, user_auth=False)
    user_id = user_data[0]['id']
    followings = CLIENT.get_users_following(user_id, expansions=None, max_results=None, pagination_token=None, tweet_fields=None, user_fields=None, user_auth=False)
    for i in followings.data:
        selfFollowingData = prospectFollowerDataMap(i.data['id'],i.data['username'],i.data['name'])
        alreadyFollowingDataMaps.append(selfFollowingData)
    return

def checkAlreadyFollowing(targetFollower, currentFollowing):
    # run a sanity check
  
    for following in currentFollowing:
        print(following)
        print('')
        print(targetFollower)
        if targetFollower == following:
            return False
        else:
            return True

def followTheFollower(target_user_id):
    CLIENT.follow_user(target_user_id, user_auth=True)


targetTwitterAccount = "CardanoProxies"
thisAccount = "BGamingHero"
selfGetCurrentFollowing(thisAccount)
friends, friendsNames = getFollowers(targetTwitterAccount)
alreadyFollowing = []
for following in alreadyFollowingDataMaps:
    alreadyFollowing.append(following['userName'])
for prospectFollower in prospectedFollowerDataMaps:
    print(prospectFollower)
    prospectFollowerName = prospectFollower['userName']
    if checkAlreadyFollowing(prospectFollowerName, alreadyFollowing):
        print(f'Already following Following { prospectFollowerName }')
        break
    else:
        print(f'Attempting to follow { prospectFollowerName }')
        followTheFollower(prospectFollower['userId'])

