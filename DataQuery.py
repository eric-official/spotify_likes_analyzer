import spotipy


def get_saved_tracks(token):
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks(limit=50)
    tracks = results['items']
    i = 0

    while results['next']:
        i += 50
        results = sp.current_user_saved_tracks(limit=50, offset=i)
        tracks.extend(results['items'])

    for item in tracks:
        track = item['track']
        #print(track['name'] + ' - ' + track['artists'][0]['name'] + ' - ' + track['id'])

    return tracks


def get_top_tracks(token):
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_tracks(time_range='long_term')
    tracks = results['items']

    for track in tracks:
        print(track['name'] + ' - ' + track['artists'][0]['name'] + ' - ' + track['id'])

    return tracks
