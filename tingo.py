import pyrebase
from devices import *

config = {
	"apiKey": "AIzaSyAn2aCD9sCRP8BR7YtRNBMns4-zBznrSf4",
	"authDomain": "tingo-eddcf.firebaseapp.com",
	"databaseURL": "https://tingo-eddcf.firebaseio.com",
	"storageBucket": "tingo-eddcf.appspot.com"
}
piID = "Garden"
firebase = pyrebase.initialize_app(config)
db = firebase.database()
ob = dict()

def stream_handler(message):
	path = message['path'].split('/')
	try:
		dev = path[1]
		if not path[2] == 'request' or len(path) < 2:
			return
	except:
		pass
		return
	type = db.child(piID).child(dev).child('type').get().val()
	args = db.child(piID).child(dev).child('args').get().val()
	typeClass = getattr(globals()[type], type)(args)
	typeClass.run(message['data'])
	db.child(piID).child(dev).update({'response': message['data']})

my_stream = db.child(piID).stream(stream_handler)
