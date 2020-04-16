import firebase_admin
from firebase_admin import credentials , firestore
cred = credentials.Certificate("Database/tk-player-firebase-adminsdk-dqi71-ede88f2491.json")
firebase = firebase_admin.initialize_app(cred)
db = firestore.client()
