import traceback

from Database.config import db


def get_artist_row():
    try:
        doc = db.collection(u'artist')
        my_ref = list(map(lambda x: x.to_dict(), list(doc.stream())))
        artists = []
        return my_ref
    except Exception as ex:
        print('Exception Occured which is of type :', ex.__class__.__name__)
        y = input('If you want to see Traceback press 1 : ')
        if y == '1':
            traceback.print_exc()
        return False


def get_artist_data():
    data = get_artist_row()
    from Database.Database import get_artist_tracks
    my_data = list(map(lambda x: get_artist_tracks(x['name']), data))
    artist_data = []
    for i in range(len(data)):
        my_dict = {
            'text': data[i]['name'],
            'url': data[i]['image_url'],
            'tracks': my_data[i]
        }
        artist_data.append(my_dict)
    return artist_data


def get_genre_data():
    from Database.Database import get_tracks_by_genre
    genre_data = get_tracks_by_genre()

    tracks_list = []
    for i in range(len(genre_data)):
        my_tracks = get_tracks_by_genre(genre=genre_data[i]['text'])
        genre_data[i]['tracks'] = my_tracks
    return genre_data


genre_data = get_genre_data()
artist_data = get_artist_data()
