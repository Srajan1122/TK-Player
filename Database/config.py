import firebase_admin
from firebase_admin import credentials , firestore
cred = credentials.Certificate("Database/3rdproject.json")
firebase = firebase_admin.initialize_app(cred)
db = firestore.client()
