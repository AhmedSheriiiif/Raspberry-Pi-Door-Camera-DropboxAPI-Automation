import dropbox

# Import libraries
import RPi.GPIO as GPIO
import time
from datetime import datetime
# GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)
# Set pin 11 as  import RPi.GPIO as GPIO

from picamera import PiCamera
from datetime import datetime
import time

camera = PiCamera()



# TIME TO START The CODE
timesets = ["11:30",
            "12:40",
            "14:20"]
# Number of seconds to open the door and get photos
NO_Of_Seconds = 10

# Access token for Dropbox
access_token = ""
dbx = dropbox.Dropbox(access_token)
  

# an output, and set servo1 as pin 11 as PWM

GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)


servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if current_time in timesets:
        print("Door Opening....")
               
        servo1.start(0)
        time.sleep(0.2)    
        #Let's move the servo!
        servo1.ChangeDutyCycle(12)
        time.sleep(0.2)
        # Run the Fan
        GPIO.output(13, GPIO.HIGH)

        # Open Camera and Get Photos
        for x in range(NO_Of_Seconds):
            photo_name = "photo-" + datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")
            filename = "/home/pi/Desktop/camera_project/photos/" + photo_name
            camera.capture(filename)
            with open(filename, 'rb') aa f:
                dbx.files_upload(f.read(), photo_name)
            time.sleep(0.5)
            
            
        #turn back to 0 degrees
        servo1.ChangeDutyCycle(2)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
        # stopping the fan
        GPIO.output(13, GPIO.LOW) 

            
        servo1.stop()
        GPIO.output(13, GPIO.LOW)
        GPIO.cleanup()
        print("Closing the Door")
    
    time.sleep(40)

