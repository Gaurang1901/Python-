import pyrebase
from datetime import *

firebaseConfig = {
  "apiKey": "AIzaSyBc4fOG7q3Nb5_-2EoukZWOYTytBV-GZz8",
  "authDomain": "proj1-7e582.firebaseapp.com",
  "databaseURL": "https://proj1-7e582-default-rtdb.firebaseio.com",
  "projectId": "proj1-7e582",
  "storageBucket": "proj1-7e582.appspot.com",
  "messagingSenderId": "405907131846",
  "appId": "1:405907131846:web:160032a16db5976db0b6c7"
};

fb = pyrebase.initialize_app(firebaseConfig)
db = fb.database()
print(db)

#id = int(input("Enter Id: "))
name = input("enter ur name ")
sal = int(input("enter ur salary:  "))
info = {"name": name, "salary":sal, "dt": str(datetime.now())}
db.child("feedback").push(info)
print("thank u ")