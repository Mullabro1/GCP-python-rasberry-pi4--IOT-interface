import tkinter as tk
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
#stop motor
def stop_motor():
    print("stop_motor clicked")
    data = {"motor": "stop"}
    db.child("gpio").set(data)
#motors 1
def motor1_fwd():
    print("motor1_fwd clicked")
    data = {"motor": "m1f"}
    db.child("gpio").set(data)

def motor1_rws():
    print("motor1_rws clicked")
    data = {"motor": "m1r"}
    db.child("gpio").set(data)
#motors 2
def motor2_fwd():
    print("motor2_fwd clicked")
    data = {"motor": "m2f"}
    db.child("gpio").set(data)

def motor2_rws():
    print("motor2_rws clicked")
    data = {"motor": "m2r"}
    db.child("gpio").set(data) 
#motors 3
def motor3_fwd():
    print("motor3_fwd clicked")
    data = {"motor": "m3f"}
    db.child("gpio").set(data) 

def motor3_rws():
    print("motor3_rws clicked")
    data = {"motor": "m3r"}
    db.child("gpio").set(data)        
#motors 4
def motor4_fwd():
    print("motor4_fwd clicked")
    data = {"motor": "m4f"}
    db.child("gpio").set(data)

def motor4_rws():
    print("motor4_rws clicked")
    data = {"motor": "m4r"}
    db.child("gpio").set(data)  
#actuator
def ack_fwd():
    print("ack_fwd clicked")
    data = {"motor": "ack_fwd"}
    db.child("gpio").set(data)

def ack_rws():
    print("ack_rws clicked")
    data = {"motor": "ack_rws"}
    db.child("gpio").set(data)  


# Create the main Tkinter window
window = tk.Tk()
window.title("Nested Boxes")
window.geometry("550x400")

# Create the outer box
outer_box = tk.LabelFrame(window, text="Robotic Arm", padx=10, pady=10, bg="cyan")
outer_box.pack(padx=10, pady=10, fill="both", expand=True)

# Create six inner boxes
inner_box1 = tk.LabelFrame(outer_box, padx=10, pady=10, bg="white")
inner_box1.grid(row=1, column=1, padx=10, pady=10)

    # Create buttons inside each inner box
button1 = tk.Button(inner_box1, text="STOP", command=stop_motor, bg="red", fg="black")
button1.pack(padx=5, pady=5)


inner_box2 = tk.LabelFrame(outer_box, text="Motor1", padx=10, pady=10, bg="white")
inner_box2.grid(row=1, column=2, padx=10, pady=10)

    # Create buttons inside each inner box
button1 = tk.Button(inner_box2, text="FORWARD", command=motor1_fwd, bg="blue", fg="white")
button1.pack(padx=5, pady=5)

button2 = tk.Button(inner_box2, text="BACKWARD", command=motor1_rws, bg="green", fg="white")
button2.pack(padx=5, pady=5)

inner_box3 = tk.LabelFrame(outer_box, text="Motor2", padx=10, pady=10, bg="white")
inner_box3.grid(row=1, column=3, padx=10, pady=10)

    # Create buttons inside each inner box
button1 = tk.Button(inner_box3, text="FORWARD", command=motor2_fwd, bg="blue", fg="white")
button1.pack(padx=5, pady=5)

button2 = tk.Button(inner_box3, text="BACKWARD", command=motor2_rws, bg="green", fg="white")
button2.pack(padx=5, pady=5)

inner_box4 = tk.LabelFrame(outer_box, text="Actuator", padx=10, pady=10, bg="white")
inner_box4.grid(row=2, column=1, padx=10, pady=10)

    # Create buttons inside each inner box
button1 = tk.Button(inner_box4, text="FORWARD", command=ack_fwd, bg="blue", fg="white")
button1.pack(padx=5, pady=5)

button2 = tk.Button(inner_box4, text="BACKWARD", command=ack_rws, bg="green", fg="white")
button2.pack(padx=5, pady=5)

inner_box5 = tk.LabelFrame(outer_box, text="Motor3", padx=10, pady=10, bg="white")
inner_box5.grid(row=2, column=2, padx=10, pady=10)

    # Create buttons inside each inner box
button1 = tk.Button(inner_box5, text="FORWARD", command=motor3_fwd, bg="blue", fg="white")
button1.pack(padx=5, pady=5)

button2 = tk.Button(inner_box5, text="BACKWARD", command=motor3_rws, bg="green", fg="white")
button2.pack(padx=5, pady=5)

inner_box6 = tk.LabelFrame(outer_box, text="Motor4", padx=10, pady=10, bg="white")
inner_box6.grid(row=2, column=3, padx=10, pady=10)

    # Create buttons inside each inner box
button1 = tk.Button(inner_box6, text="FORWARD", command=motor4_fwd, bg="blue", fg="white")
button1.pack(padx=5, pady=5)

button2 = tk.Button(inner_box6, text="BACKWARD", command=motor4_rws, bg="green", fg="white")
button2.pack(padx=5, pady=5)


# Run the Tkinter event loop
window.mainloop()