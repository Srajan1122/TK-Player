import firebase_admin
from firebase_admin import credentials , firestore
cred = credentials.Certificate("Database/tk-player-firebase-adminsdk-dqi71-eab39013d1.json")
firebase = firebase_admin.initialize_app(cred)
db = firestore.client()
