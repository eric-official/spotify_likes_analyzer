import spotipy.util as util


def create_token(username, scope):  # scope='user-library-read'

    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    redirect_uri = 'YOUR_REDIRECT_URI'
    token = util.prompt_for_user_token(username=username,
                                       scope=scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri)
    return token


def get_ids(tracklist):

    id_list = []
    for item in tracklist:
        track = item['track']
        id_list.append(track['id'])
    return id_list
