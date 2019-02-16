import folium
from twitter_utils import get_friends, get_coordinates
import os


def build_map(user_name, limit):
    friends = get_friends(user_name)
    if friends == None:
        return None
    friends_name = list(map(lambda x: x[0], friends))
    coordinates = []
    locations = []
    for friend in friends:
        location = friend[-1]
        locations.append(location)
        coordinate = get_coordinates(location)
        coordinates.append(coordinate)
    filtered_list = list(
        filter(lambda x: x[0] != None and x[1] != '', list(zip(coordinates, locations, friends_name))))
    if limit is not None:
        filtered_list = filtered_list[:limit]
    friends_map = folium.Map(zoom_start=10)
    coordinates = list(map(lambda x : x[0], filtered_list))
    locations = list(map(lambda x: x[1], filtered_list))
    friends_name = list(map(lambda x: x[2], filtered_list))
    for [lt, ln], location, name in zip(coordinates, locations, friends_name):
        marker = folium.Marker(location=[lt, ln], popup=' in '.join(
            [name, location]), icon=folium.Icon())
        friends_map.add_child(marker)
    path = os.sep.join(['templates', user_name + 'map.html'])
    friends_map.save(path)
    return user_name + 'map.html'
