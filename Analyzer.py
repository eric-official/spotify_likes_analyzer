from typing import Dict

import spotipy


def avg_features(token, tracklist):
    sp = spotipy.Spotify(auth=token)
    track_counter: int = 0
    danceability = 0
    energy = 0
    loudness = 0
    speechiness = 0
    acousticness = 0
    instrumentalness = 0
    liveness = 0
    valence = 0
    tempo = 0

    lower=0
    upper=99
    track_features=[]

    while tracklist[lower:upper]:
        track_features += sp.audio_features(tracks=tracklist[lower:upper])
        lower+=100
        upper+=100

    for track_feature in track_features:
        danceability += track_feature['danceability']
        energy += track_feature['energy']
        loudness += track_feature['loudness']
        speechiness += track_feature['speechiness']
        acousticness += track_feature['acousticness']
        instrumentalness += track_feature['instrumentalness']
        liveness += track_feature['liveness']
        valence += track_feature['valence']
        tempo += track_feature['tempo']
        track_counter += 1

    print("number of liked songs:", track_counter)

    danceability /= track_counter
    energy /= track_counter
    loudness /= track_counter
    speechiness /= track_counter
    acousticness /= track_counter
    instrumentalness /= track_counter
    liveness /= track_counter
    valence /= track_counter
    tempo /= track_counter
    print("average tempo: %.2f" % tempo)

    feature_list: Dict[str, int] = {'danceability': danceability, 'energy': energy, 'loudness': loudness,
                                    'speechiness': speechiness, 'acousticness': acousticness,
                                    'instrumentalness': instrumentalness, 'liveness': liveness, 'valence': valence}

    return feature_list


def relative_features(feature_list):

    feature_list['danceability'] *= 100
    feature_list['energy'] *= 100
    feature_list['loudness'] = ((feature_list['loudness']*(-1.0))/60)*100
    feature_list['speechiness'] *= 100
    feature_list['acousticness'] *= 100
    feature_list['instrumentalness'] *= 100
    feature_list['liveness'] *= 100
    feature_list['valence'] *= 100
    #feature_list['tempo'] = (feature_list['tempo']/250)*100

    return feature_list
