import pyrebase

# Config/Setup
#-------------------------------------------------------------------------------
firebaseConfig = {
    "apiKey": "AIzaSyAqjmrD93q0u33rILEK316BQ3YJcXPDmdE",
    "authDomain": "test-iot-afb68.firebaseapp.com",
    "projectId": "test-iot-afb68",
    "databaseURL": "https://test-iot-afb68-default-rtdb.firebaseio.com/",
    "storageBucket": "test-iot-afb68.appspot.com",
    "messagingSenderId": "45153370739",
    "appId": "1:45153370739:web:c1410a5f3d4d2ef047e006"  
 }
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
cli = input("dev cli options: \n stop \n m1f \n m1r\n m2f \n m2r \n m3f \n m3r \n m4f \n m4r \n ack_fwd \n ack_rws \n enter the input: \n")

data = {"motor": cli}

db.child("gpio").set(data)