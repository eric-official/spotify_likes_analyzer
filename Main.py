from Analyzer import *
from DataQuery import *
from UtilClass import *
from Visualizer import *

token = create_token('eric_official', 'user-library-read')
tracks = get_saved_tracks(token)
ids = get_ids(tracks)
features = avg_features(token, ids)
features: dict = relative_features(features)
show_radar_graph(features)

