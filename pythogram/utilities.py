
def get_total_followers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    followers = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''

        response = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers


def get_total_followings(api, user_id):
    """
    Returns the list of followings of the user.
    It should be equivalent of calling api.getTotalFollowings from InstagramAPI
    """

    followings = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''

        response = api.getUserFollowings(user_id, maxid=next_max_id)
        followings.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followings
