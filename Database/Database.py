from Database.config import *
import traceback
import tkinter as tk
from tkinter import messagebox



def get_tracks_by_language(**kwargs):
	"""
	Returns a list of songs with particular language
	kwarg : language = 'required language'
	else return the list of all languages
	if failed returns false
	"""
	if 'language' in kwargs:
		try:
			doc_ref = db.collection('Tracks')
			snapshots = list(doc_ref.where(u'Language', u'==', kwargs['language']).stream())
			if len(snapshots):
				object_list = list(map(lambda x: x.to_dict(), snapshots))
				
				return object_list
		except Exception as ex:
			messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
			print('Exception Occurred which is of type :', ex.__class__.__name__)
			y = input('If you want to see Traceback press 1 : ')
			if y == '1':
				traceback.print_exc()
			return False
	else:
		try:
			doc_ref = db.collection(u'languages').stream()
			object_list = list(map(lambda x: x.to_dict(), doc_ref))
		
			all_dicts = []
			for i in range(len(object_list)):
				my_dict = {
					'text': object_list[i]['language_name'],
					 'url': object_list[i]['language_image'],
				}
				all_dicts.append(my_dict)
			
			return all_dicts
		except Exception as ex:
			messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
			
			print('Exception Occurred which is of type :', ex.__class__.__name__)
			y = input('If you want to see Traceback press 1 : ')
			if y == '1':
				traceback.print_exc()
			return False



def get_artist_tracks(artist):
	"""
	Returns a list of the objects of tracks
	if the artist exist or else returns False

	"""
	try:
		doc_ref = db.collection(u'artist/' + artist + '/tracks')
		if list(doc_ref.stream()) is None:
			raise Exception('Not such artist registered')
		tracks = list(map(lambda x: x.to_dict(), list(doc_ref.stream())))
		return tracks
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False



def get_track(trackName):
	"""
	Fetch particular track for user
	returns dictitonary with the keys as
	artist, genre, location , title
	if failed returns false
	"""
	try:
		doc_ref = db.collection(u'Tracks').document(trackName)
		if doc_ref.get().to_dict() is None:
			raise Exception("No such track found")
		return doc_ref.get().to_dict()
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False


def register_user(username, email, phone_number, password):
	"""
	Returns user uid if successfully registered
	else returns false
	"""
	from firebase_admin import auth
	try:
		if username == '' or email == '' or phone_number == '':
			raise Exception('Some of fields were found to be empty')
		elif len(password) <= 6:
			raise Exception('Password length less then equal to 6')
		user = auth.create_user(
			email=email,
			phone_number='+91' + phone_number,
			password=password,
			display_name=username,
			email_verified = False,

		)
		doc_ref = db.collection(u'users').document(user.uid)
		doc_ref.set({
			'email': email,
			'phone_number': '+91' + phone_number,
			'password': password,
			'display_name': username,
			'email_verified':False
		})
		
		return user.uid
	except firebase_admin._auth_utils.EmailAlreadyExistsError as ex:
		from Pages.UserAuthentication.Exceptions import Email_already_exists
		Email_already_exists()
		return False
	except firebase_admin._auth_utils.PhoneNumberAlreadyExistsError as ex:
		from Pages.UserAuthentication.Exceptions import Phone_already_exists
		Phone_already_exists()
		return False
	except firebase_admin._auth_utils.UserNotFoundError as ex:
		from Pages.UserAuthentication.Exceptions import User_not_Found
		User_not_Found()
		return False
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False





def get_all_tracks():
	"""
	Returns a list of all track objects
	if failed returns a false
	"""
	try:
		collection = db.collection(u'Tracks')
		return list(map(lambda x: x.to_dict(), collection.stream()))
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False


def get_tracks_by_genre(**kwargs):
	"""
	Returns a list of songs with particular genre
	kwarg : genre = 'required genre'
	else return the list of all genres
	if failed returns false
	"""
	if 'genre' in kwargs:
		try:
			doc_ref = db.collection('Tracks')
			snapshots = list(doc_ref.where(u'genre', u'==', kwargs['genre']).stream())
			if len(snapshots):
				object_list = list(map(lambda x: x.to_dict(), snapshots))
				
				return object_list
		except Exception as ex:
			messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
			print('Exception Occurred which is of type :', ex.__class__.__name__)
			y = input('If you want to see Traceback press 1 : ')
			if y == '1':
				traceback.print_exc()
			return False
	else:
		try:
			doc_ref = db.collection(u'genres').stream()
			object_list = list(map(lambda x: x.to_dict(), doc_ref))
		
			all_dicts = []
			for i in range(len(object_list)):
				my_dict = {
					'text': object_list[i]['genre_name'],
					 'url': object_list[i]['genre_image'],
				}
				all_dicts.append(my_dict)
		
			return all_dicts
		except Exception as ex:
			messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
			
			print('Exception Occurred which is of type :', ex.__class__.__name__)
			y = input('If you want to see Traceback press 1 : ')
			if y == '1':
				traceback.print_exc()
			return False


def get_user(uid):
	"""
	Returns a user object that is dictionary
	of the user with attributes:
	display_name , email , password, phone_number
	"""
	# [START get_user]
	from firebase_admin import auth
	try:
		user = auth.get_user(uid)
		
		doc = db.collection(u'users').document(user.uid)
		doc = doc.get().to_dict()
		return doc
	except firebase_admin._auth_utils.UserNotFoundError as ex:
		from Pages.UserAuthentication.Exceptions import User_not_Found
		User_not_Found()
		return False
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False

	# [END get_user]


def get_user_by_email(email):
	"""
	Returns a user object that is dictionary
	of the user with attributes:
	display_name , email , password, phone_number
	"""
	# [START get_user_by_email]
	import firebase_admin
	from firebase_admin import auth 
	try:

		user = auth.get_user_by_email(email)
		doc = db.collection(u'users').document(user.uid)
		doc = doc.get().to_dict()
		return doc
	except firebase_admin._auth_utils.UserNotFoundError as ex:
		from Pages.UserAuthentication.Exceptions import User_not_Found
		User_not_Found()
		return False
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False


def get_user_by_phone_number(phone):
	"""
	Returns a user object that is dictionary
	of the user with attributes:
	display_name , email , password, phone_number
	"""

	from firebase_admin import auth
	try:
		user = auth.get_user_by_phone_number(phone)
		doc = db.collection(u'users').document(user.uid)
		doc = doc.get().to_dict()
		return doc
	
	except firebase_admin._auth_utils.UserNotFoundError as ex:
		from Pages.UserAuthentication.Exceptions import User_not_Found
		User_not_Found()
		return False
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False

		# [END get_user_by_phone]





def sign_in_with_email_and_password(email, password):
	"""
	Returns boolean True if user is signed in succesfully
	else false
	"""
	from os import path

	try:
		if path.exists('user'):
			f = open('user', 'r')
			doc = get_user(f.readline())
			f.close()
			return doc
		from firebase_admin import auth
		user = auth.get_user_by_email(email)
		doc = get_user_by_email(email)
		if doc['email'] == email and doc['password'] == password:
			f = open('user', "w+")
			f.write(user.uid)
			return doc
		else:
			from Pages.UserAuthentication.Exceptions import Invalid_credentials
			Invalid_credentials()

			# return False
	except firebase_admin._auth_utils.UserNotFoundError as ex:
		from Pages.UserAuthentication.Exceptions import User_not_Found
		User_not_Found()
		return False
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False


def sign_out():
	"""

	returns True
	if signed out else false
	also remove the user files

	"""
	import os
	try:
		os.remove("user")
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occured which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False

	# sign_out()
# myuser = register_user('devdatta','dkhoche70@gmail.com','9145253235','15412342')
def generate_otp(uid):
	import string
	import random

	# Takes random choices from
	# ascii_letters and digits
	try:
		generate_pass = ''.join([random.choice(
											   string.digits)
								 for n in range(6)])

		doc_ref = db.collection(u'users').document(uid)
		doc_ref.update({
			'verification_code'  : generate_pass
		})
	
		return generate_pass
	except firebase_admin._auth_utils.UserNotFoundError as ex:
		from Pages.UserAuthentication.Exceptions import User_not_Found
		User_not_Found()
		return False
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False


def check_verification(email):
	user  = get_user_by_email(email)
	return user['email_verified']


def send_email_verification_otp(email):
	'''

	:param otp:
		   email: email of the user
	:return: bool


	'''
	try:
		from firebase_admin import auth
		
		import smtplib
		user = auth.get_user_by_email(email)
		otp = generate_otp(user.uid)
		fromaddr = 'amplifyteam1234@gmail.com.'
		toaddrs = email
		Text = 'Hello '+ user.display_name  + ',\nEnter the following OTP to verify your email address. \nYour verification code is '+otp+'\nIf you didn’t ask to verify this address, you can ignore this email.\nThanks,\nYour AmplifyTeam'
		subject = 'Email Verification'
		username = 'amplifyteam1234@gmail.com'
		password = '15412342'
	
		message = 'Subject: {}\n\n{}'.format(subject, Text)
		message = message.encode()
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(username, password)
		server.sendmail(fromaddr, toaddrs, message)
		messagebox.showinfo('Info','Please enter the OTP \nsent to your email.')
		server.quit()
	except firebase_admin._auth_utils.UserNotFoundError as ex:
		from Pages.UserAuthentication.Exceptions import User_not_Found
		User_not_Found()
		return False
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False


def generate_password(uid):
	import random
	import string

	
	letters = string.ascii_lowercase
	password = ''.join(random.choice(letters) for i in range(10))
	doc_ref = db.collection(u'users').document(uid)
	doc_ref.update({
			'password'  :  password
		})
	return password



def Forget_password_email(email):
	'''

	:param otp:
		   email: email of the user
	:return: bool


	'''
	try:
		from firebase_admin import auth
		
		import smtplib
		
		user = auth.get_user_by_email(email)
		password = generate_password(user.uid)
		fromaddr = 'amplifyteam1234@gmail.com.'
		toaddrs = email
		Text = 'Hello '+ user.display_name  + ',\nThis is your new password now on. \nYour new password is '+password+'.\nMake sure you don"t forget it.\nThanks,\nYour AmplifyTeam'
		subject = 'New Password Request'
		username = 'amplifyteam1234@gmail.com'
		password = '15412342'
		
		message = 'Subject: {}\n\n{}'.format(subject, Text)
		message = message.encode()
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(username, password)
		server.sendmail(fromaddr, toaddrs, message)
		messagebox.showinfo('Info','Please enter the new password \nsent to your email.')
		server.quit()
	except ValueError :
				messagebox.showerror('Error','Please Enter email.')
	except firebase_admin._auth_utils.UserNotFoundError as ex:
	    from Pages.UserAuthentication.Exceptions import User_not_Found
	    User_not_Found()
	    return False
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occurred which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False

def verify_email_database(email,entered_otp):
	'''
	Verifies if the OTP is correct 
	Returns bool depending on Success
	'''
	
	from firebase_admin import auth
	user = auth.get_user_by_email(email)
	db_user = get_user_by_email(email)
	if entered_otp == db_user['verification_code']:
		auth.update_user(user.uid, email_verified = True)
		doc_ref = db.collection(u'users').document(user.uid)
		doc_ref.update({
			'email_verified': True
		})
		return True
	else:
		return False

# send_email_verification_otp('dkhoche2000@gmail.com')



def add_liked_songs(track_object,uid):
	'''

	params : track_object : The object of the track
		   : uid : unique Identification No. of the user
	return Bool

	'''
	try:
		collection = db.collection(u'users/'+uid+'/Liked_songs').document(track_object['title'])
		collection.set(track_object)
		add_like_count(track_object['title'])
		
		return True
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occured which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False

def delete_liked_song(uid,track_title):
	'''

	params : track title : The title of the track to be deleted
		   : uid : unique Identification No. of the user
	return Bool

	'''
	try:
		collection = db.collection(u'users/'+uid+'/Liked_songs').document(track_title)
		collection.delete()
		decrease_like_count(track_title)
	
		return True
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occured which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False

def get_all_liked_songs(uid): 
	try:
		collection = db.collection(u'users/'+uid+'/Liked_songs')
	
		return list(map(lambda x: x.to_dict(), collection.stream()))
		
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occured which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False


	

def order_simple_trending_song():
	'''
	Returns list of songs in the descending order

	'''
	try:
		doc_ref = db.collection(u'Tracks')
		query = doc_ref.order_by(
			u'like_count', direction=firestore.Query.DESCENDING)
		results = query.stream()
		
		return list(map(lambda x: x.to_dict(), results))
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occured which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False
		

def add_like_count(title):
	try:
		myobject = get_track(title)
		doc_ref  = db.collection(u'Tracks').document(title)
		doc_ref.update({
			'like_count' : myobject['like_count'] + 1
		})
		doc_ref = db.collection(u'artist/'+myobject['artist']+'/tracks').document(title)
		doc_ref.update({
			'like_count' : myobject['like_count'] + 1 

		})
		return True
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occured which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False


def decrease_like_count(title):
	try:
		myobject = get_track(title)
		doc_ref  = db.collection(u'Tracks').document(title)
		doc_ref.update({
			'like_count' : myobject['like_count'] - 1
		})
		doc_ref = db.collection(u'artist/'+myobject['artist']+'/tracks').document(title)
		doc_ref.update({
			'like_count' : myobject['like_count'] - 1 

		})
		return True
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occured which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False


def get_genre(genre_name):
	'''
	parameters: artist name
	output:return the dictionary with key genre_name ,genre_image
	'''
	try:
		doc_ref = db.collection(u'genres').document(genre_name)
		data=doc_ref.get().to_dict()
	
		return data
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occured which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False

def get_artist(artist_name):
	'''
	parameters: artist name
	output:return the dictionary with key name ,image_url
	'''
	try:
		doc_ref = db.collection(u'artist').document(artist_name)
		data=doc_ref.get().to_dict()
		
		return data
	except Exception as ex:
		messagebox.showerror('Error','Oops!! Something went wrong!!\nTry again later.')
		
		print('Exception Occured which is of type :', ex.__class__.__name__)
		y = input('If you want to see Traceback press 1 : ')
		if y == '1':
			traceback.print_exc()
		return False