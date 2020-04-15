from config import *
import traceback; 




def set_artist(track_title,track_genre,track_location,track_artist):
    '''
    Function to set only artist details
    Returns boolean True if set else False
    gets invoked in the get song function 
    '''
    
    try:
        collection = db.collection(u'artist').document(track_artist)
        collection.set({
            'name' : track_artist
        })
        artistTracks = db.collection(u'artist/'+track_artist+'/tracks').document(track_title)
        artistTracks.set({
            'title' : track_title,
            'genre': track_genre,
            'location':track_location

        })
        print('artist added')
        return True
    except Exception as ex:
        print('Exception Occured which is of type :', ex.__class__.__name__)
        y = input('If you want to see Traceback press 1 : ')
        if(y == '1'):
            traceback.print_exc();    
        return False

def Check_artist(artist):
    '''
    Returns boolean value if the artist exist or not in the database
    '''
    try:
        doc_ref = db.collection(u'artist').document(artist)
        if(doc_ref.get().to_dict() == None):
            raise Exception('Not such artist registered')
        print('Artist got successfully')
        return True
    except Exception as ex:
        print('Exception Occured which is of type :', ex.__class__.__name__)
        y = input('If you want to see Traceback press 1 : ')
        if(y == '1'):
            traceback.print_exc();    
        return False

def get_artist_tracks(artist):
    '''
    Returns a list of the objects of tracks
    if the artist exist or else returns False

    '''
    try:
        doc_ref = db.collection(u'artist/'+artist+'/tracks')
        if(list(doc_ref.stream()) == None):
            raise Exception('Not such artist registered')
        tracks = list(map(lambda x: x.to_dict(),list(doc_ref.stream())))
        return tracks
    except Exception as ex:
        print('Exception Occured which is of type :', ex.__class__.__name__)
        y = input('If you want to see Traceback press 1 : ')
        if(y == '1'):
            traceback.print_exc();    
        return False



def set_track(track_title,track_genre,track_location,track_artist):
    '''
    Function to set only track details
    Returns boolean depending if the value is succesfully set then 'True' else 'False'

    '''
    if(track_artist == '' or track_genre == '' or track_location == '' or track_title == ''):
        raise Exception('Cannot generate with empty Field')
    try:
        collection = db.collection(u'Tracks').document(track_title)
        collection.set({
            'artist' : track_artist,
            'genre': track_genre,
            'location': track_location,
            'title':track_title
        })
        print('Track added successfully')
        set_artist(track_title,track_genre,track_location,track_artist)
        return True
    except Exception as ex:
        print('Exception Occured which is of type :', ex.__class__.__name__)
        y = input('If you want to see Traceback press 1 : ')
        if(y == '1'):
            traceback.print_exc();    
        return False
    



def get_track(trackName):
    '''
    Fetch particular track for user 
    returns dictitonary with the keys as 
    artist, genre, location , title
    if failed returns false

    '''
    try:
        doc_ref = db.collection(u'Tracks').document(trackName)
        if(doc_ref.get().to_dict() == None):
            raise Exception("No such track found")
        return doc_ref.get().to_dict()
    except Exception as ex:
        print('Exception Occured which is of type :', ex.__class__.__name__)
        y = input('If you want to see Traceback press 1 : ')
        if(y == '1'):
            traceback.print_exc();    
        return False

def register_user(Username,email,phone_number,password):

    '''
    Returns user uid if successfully registered
    else returns false

    '''
    from firebase_admin import auth
    try:
        if(Username == ''or email== '' or phone_number == ''):
            raise Exception('Some of fields were found to be empty')
        elif len(password) <= 6 :
            raise Exception('Password length less then equal to 6')
        user = auth.create_user(
        email=email,
        phone_number='+91'+phone_number,
        password=password,
        display_name=Username,
        )
        doc_ref = db.collection(u'users').document(user.uid)
        doc_ref.set({
            'email' : email,
        'phone_number' : '+91'+phone_number,
        'password'  : password,
        'display_name'  : Username,
        })
        print('Sucessfully created new user: {0}'.format(user.uid))
        return user.uid
    except Exception as ex:
        print('Exception Occured which is of type :', ex.__class__.__name__)
        y = input('If you want to see Traceback press 1 : ')
        if(y == '1'):
            traceback.print_exc();    
        return False
    

def set_album(track_title,album_name,artist):

    '''
 Returns boolean value depending upon success
 and atleast one track in needed for the album.
    '''
    try:
        track_object = get_track(track_title)
        doc_ref = db.collection(u'albums/'+album_name+'/tracks').document(track_object['title'])
        doc_ref.set(track_object)
        doc_ref = db.collection(u'albums').document(album_name)
        doc_ref.set({
            'album_title' : album_name,
            'artist': artist
        })
        print('Album Created Successfully')
        return True
    except Exception as ex:
        print('Exception Occured which is of type :', ex.__class__.__name__)
        y = input('If you want to see Traceback press 1 : ')
        if(y == '1'):
            traceback.print_exc();    
        return False




def get_album(**kwargs):
    '''
    parameters : album_name, artist_name
    if want all the albums dont pass any argument else pass name of the album or artist of the album.
    eg:- get_album(album_name = devdatta)
    Kwargs : album_name 
    '''

    if 'album_name' in kwargs:
        try:
            doc_ref = db.collection(u'albums/'+kwargs['album_name']+'/tracks')
            snapshots = list(doc_ref.stream())
            if len(snapshots):
                tracks = list(map(lambda x : x.to_dict(),snapshots))
                return tracks
        except Exception as ex:
            print('Exception Occured which is of type :', ex.__class__.__name__)
            y = input('If you want to see Traceback press 1 : ')
            if(y == '1'):
                traceback.print_exc();    
            return False
    elif 'artist' in kwargs:
        try:
            doc_ref = db.collection('albums')
            snapshots = list(doc_ref.where(u'artist', u'==',kwargs['artist']).stream())
            
            if len(snapshots):
                    object_list = list(map(lambda x : x.to_dict(),snapshots))
                    return object_list
            else :
                raise Exception('No data with the give artist found')
        except Exception as ex:
            print('Exception Occured which is of type :', ex.__class__.__name__)
            y = input('If you want to see Traceback press 1 : ')
            if(y == '1'):
                traceback.print_exc();    
            return False
    else : 
        try:
            collection = db.collection(u'albums')
            print(list(map(lambda x : x.to_dict(),collection.stream()))) 
        except Exception as ex:
            print('Exception Occured which is of type :', ex.__class__.__name__)
            y = input('If you want to see Traceback press 1 : ')
            if(y == '1'):
                traceback.print_exc();    
            return False


                 
def get_all_tracks():
    '''
    Returns a list of all track objects
    if failed returns a false

    '''
    try:
        collection = db.collection(u'Tracks')
        return list(map(lambda x : x.to_dict(),collection.stream()))
    except Exception as ex:
        print('Exception Occured which is of type :', ex.__class__.__name__)
        y = input('If you want to see Traceback press 1 : ')
        if(y == '1'):
            traceback.print_exc();    
        return False 


def get_tracks_by_genre(**kwargs):
    '''
    Returns a list of songs with particular genre 
    kwarg : genre = 'required genre'
    else return the list of all genres
    if failed returns false

    '''
    if 'genre' in kwargs:
        try:
            doc_ref = db.collection('Tracks')
            snapshots = list(doc_ref.where(u'genre', u'==',kwargs['genre']).stream())
            if len(snapshots):
                object_list = list(map(lambda x : x.to_dict(),snapshots))
                print(object_list)
                return
        except Exception as ex:
            print('Exception Occured which is of type :', ex.__class__.__name__)
            y = input('If you want to see Traceback press 1 : ')
            if(y == '1'):
                traceback.print_exc();    
            return False 
    else:
        try:
            doc_ref = db.collection('Tracks').stream()
            object_list = list(map(lambda x : x.to_dict(),doc_ref))
            genre_list = []
            for i in object_list:
                if i['genre'] not in genre_list:
                    genre_list.append(i['genre'])
            return genre_list
        except Exception as ex:
            print('Exception Occured which is of type :', ex.__class__.__name__)
            y = input('If you want to see Traceback press 1 : ')
            if(y == '1'):
                traceback.print_exc();    
            return False 
                
def get_user(uid):
    '''

    Returns a user object that is dictionary 
    of the user with attributes: 
    display_name , email , password, phone_number


    '''
    # [START get_user]
    from firebase_admin import auth
    try:
        user = auth.get_user(uid)
        print('Successfully fetched user data: {0}'.format(user.uid))
        doc = db.collection(u'users').document(user.uid)
        doc = doc.get().to_dict()
        return doc
    except Exception as ex:
        print('Exception Occured which is of type :', ex.__class__.__name__)
        y = input('If you want to see Traceback press 1 : ')
        if(y == '1'):
            traceback.print_exc();    
        return False

    # [END get_user]

def get_user_by_email(email):
    '''
    Returns a user object that is dictionary 
    of the user with attributes: 
    display_name , email , password, phone_number

    '''
    # [START get_user_by_email]
    from firebase_admin import auth
    try:
        
        user = auth.get_user_by_email(email)
        doc = db.collection(u'users').document(user.uid)
        doc = doc.get().to_dict()
        return doc
    except Exception as ex:
        print('Exception Occured which is of type :', ex.__class__.__name__)
        y = input('If you want to see Traceback press 1 : ')
        if(y == '1'):
            traceback.print_exc();    
        return False 
    # [END get_user_by_email]


def get_user_by_phone_number(phone):
    '''
    Returns a user object that is dictionary 
    of the user with attributes: 
    display_name , email , password, phone_number

    '''
    
    from firebase_admin import auth
    try:
        user = auth.get_user_by_phone_number(phone)
        doc = db.collection(u'users').document(user.uid)
        doc = doc.get().to_dict()
        return doc
    except Exception as ex:
        print('Exception Occured which is of type :', ex.__class__.__name__)
        y = input('If you want to see Traceback press 1 : ')
        if(y == '1'):
            traceback.print_exc();    
        return False 

    # [END get_user_by_phone]

def sign_in_with_phone():
    pass
def sign_in_with_email_and_password(email,password):

    '''
    Returns boolean True if user is signed in succesfully
    else false

    '''
    try:
        from firebase_admin import auth
        user = auth.get_user_by_email(email)
        doc = get_user_by_email(email)
        if(doc['email'] == email and doc['password'] == password):
           f  = open('user',"w+")
           f.write(user.uid)
           return True
        else:
            raise Exception('Credentials invalid')
            return False 
    except Exception as ex:
        print('Exception Occured which is of type :', ex.__class__.__name__)
        y = input('If you want to see Traceback press 1 : ')
        if(y == '1'):
            traceback.print_exc();    
        return False 

def sign_out():

    '''

    returns True
    if signed out else false
    also remove the user files 

    '''
    import os
    try : 
        os.remove("user")
    except Exception as ex:
        print('Exception Occured which is of type :', ex.__class__.__name__)
        y = input('If you want to see Traceback press 1 : ')
        if(y == '1'):
            traceback.print_exc();    
        return False 

    


# sign_in_with_email_and_password('dkhoche70@gmail.com','15412342')
# sign_out()
# myuser = register_user('devdatta','dkhoche70@gmail.com','9145253235','15412342')
