import spotipy.util as util


def create_token(username, scope):  # scope='user-library-read'

    client_id = '9e081501ea5b4564bfd7e424762e756a'
    client_secret = '04150d528cd5471dac96be12d55dcac7'
    redirect_uri = 'http://localhost:8888/callback'
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
