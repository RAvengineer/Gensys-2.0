from flask import render_template, request, Response,jsonify
from Genesys_v2 import app
from Utilities.CamFeed import CamFeed

# Variables
cameraNumber = 0

# TODO: Remove later
from random import uniform


# Routes for Templates
@app.route('/')
@app.route('/Genesys_v2')
def genesys_v2():
    return render_template('base.html')


@app.route('/autonomous')
def autonomous():
    return render_template('autonomous.html')


@app.route('/manual')
def manual():
    return render_template('manual.html')


@app.route('/science')
def science():
    return render_template('science.html')


# Routes for Responsive WebPages
@app.route('/video_feed')
def video_feed():
    camera = CamFeed()
    return Response(camera.gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/changeCamera',methods=['POST'])
def changeCamera():
    global cameraNumber
    # method = GET
    # request.args returns ImmutableMultiDict type
    # print(request.args) gives ImmutableMultiDict([('{"cameraNumber":"2"}', '')])
    # print(request.args.to_dict()) gives {'{"cameraNumber":"2"}': ''}
    # print(list(request.args.to_dict().keys()))
    # method = POST
    # print(request.json['cameraNumber']) gives '2'
    # print(request.get_json()) gives {'cameraNumber': '2'}
    
    cameraNumber = request.json['cameraNumber'] # type(cameraNumber): <class 'str'>
    print("Camera Number Selected:",cameraNumber)
    return jsonify(status="changed")

@app.route('/getGamepadKeys')
def getGamepadKeys():
    return jsonify(
        mode="baseMotors",
        command="STOP"
    )

@app.route('/addGPS')
def addGPS():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/getElectricalGpsValues')
def getElectricalGpsValues():
    current_gps = "CURRENT_GPS"
    battery1 = round(uniform(20.0,24.0),1)
    battery2 = round(uniform(20.0,24.0),1)
    motor1 = round(uniform(0.0,5.0),1)
    motor2 = round(uniform(0.0,5.0),1)
    motor3 = round(uniform(0.0,5.0),1)
    motor4 = round(uniform(0.0,5.0),1)
    motor5 = round(uniform(0.0,5.0),1)
    motor6 = round(uniform(0.0,5.0),1)
    return jsonify(
        current_gps = current_gps,
        battery1=battery1,
        battery2=battery2,
        motor1=motor1,
        motor2=motor2,
        motor3=motor3,
        motor4=motor4,
        motor5=motor5,
        motor6=motor6
    )
"""
TODO 1: Take gamepad values
        SetInterval for calling the route '/gamepadEvents'
        Create a class in Utilities for Gamepad Events
        Distinguish the controls using if case, ex. ('base','forward'), ('arm','AC1')
        Jsonify and send it to the client and display in the motors status
TODO 2: update values periodically
        Socket
TODO 3: addGPS
TODO 4: Autonomous --DONE
        Detection Status(left arrow, right arrow, ball) --Done
        Status Button For Autonomous --Done
TODO 5: Hotkey Commands for Science(0-9) --DONE
TODO 6: Fail Safe for Gamepad
        Also, add a code for controlling the rover through keyboard
"""

# Read for understanding the return type of request.form: https://werkzeug.palletsprojects.com/en/0.15.x/datastructures/
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == "POST":
        # Request the forms to return the inputs in form of dictionary
        pins_dict = request.form.to_dict() # Output: dict_keys(['dp0', 'dp3', 'dp6', 'ap0', 'ap4'])
        print(pins_dict)

        # Create an empty list for digital pins
        digital_pins = []
        # Create an empty list for analog pins
        analog_pins = []

        # print(pins_dict.keys()) # Debugging

        # Append the pin numbers in their appropriate lists
        for pin in list(pins_dict.keys()):
            if('dp' in pin):
                digital_pins.append(int(pin[2:]))
            elif('ap' in pin):
                analog_pins.append(int(pin[2:]))
        
        # Debugging
        # print(digital_pins)
        # print(analog_pins)
    return render_template('upload.html')


@app.route('/user/<username>')
def profile(username):
    print(f'The username is {username}')
    return f'<h1>{username}<h1>'
