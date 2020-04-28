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

def get_language_data():
    from Database.Database import get_tracks_by_language
    language_data = get_tracks_by_language()

    tracks_list = []
    for i in range(len(language_data)):
        my_tracks = get_tracks_by_language(language=language_data[i]['text'])
        language_data[i]['tracks'] = my_tracks
    return language_data

def Top_hits_data():
    from Database.Database import  order_simple_trending_song
    data = order_simple_trending_song()
    my_dict = {
        'text':'Top Hits',
        'url':'https://firebasestorage.googleapis.com/v0/b/another-tk-player.appspot.com/o/Top%20Hits.jpg?alt=media&token=38eec66b-9bf9-455c-b24f-d8cdf6906186',
        'tracks':data
    }
    my_list = []
    my_list.append(my_dict)
    return my_list

genre_data = get_genre_data()
artist_data = get_artist_data()
language_data = get_language_data()
Trending_data = Top_hits_data()
