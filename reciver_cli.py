# Imports
#-------------------------------------------------------------------------------
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

test = db.child("gpio").get()

for test in test.each():
    f= test.val()
    print(f)
      
if f == 'stop':
    print("stop")
    db.child("gpio").child("motor").remove()#stop
elif f == "ack_fwd":
    print("ack_fwd")
    db.child("gpio").child("motor").remove()#actuators
elif f == "ack_rws":
    print("ack_rws")
    db.child("gpio").child("motor").remove()#actuators
elif f == "m1f":
    print("m1f")
    db.child("gpio").child("motor").remove()#motor1
elif f == "m1r":
    print("m1r")
    db.child("gpio").child("motor").remove()#motor1 
elif f == "m2f":
    print("m2f")
    db.child("gpio").child("motor").remove()#motor2
elif f == "m2f":
    print("m2f")
    db.child("gpio").child("motor").remove()#motor2
elif f == "m3f":
    print("m3f")
    db.child("gpio").child("motor").remove()#motor3
elif f == "m3r":
    print("m3r")
    db.child("gpio").child("motor").remove()#motor3
elif f == "m4f":
    print("m4f")
    db.child("gpio").child("motor").remove()#motor4
elif f == "m4r":
    print("m4r")
    db.child("gpio").child("motor").remove()#motor4
else:
    print("database input invalid")#database connection issue














































#db.child("gpio").get()

#data = {"Age": 21, "Name": "Jenna", "Employed": True}
#-------------------------------------------------------------------------------
# Create Data

#db.push(data)
#db.child("Users").child("FirstPerson").set(data)

#-------------------------------------------------------------------------------
# Read Data

#jenna = db.child("Users").child("FirstPerson").get()
#print(jenna.val())
#-------------------------------------------------------------------------------
# Update Data

#db.child("Users").child("FirstPerson").update({"Name": "Larry"})

#-------------------------------------------------------------------------------
# Remove Data

#Delete 1 Value
#db.child("Users").child("FirstPerson").child("Age").remove()

# Delete whole Node
#db.child("Users").child("FirstPerson").remove()

#-------------------------------------------------------------------------------