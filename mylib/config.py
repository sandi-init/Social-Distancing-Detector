# base path to YOLO directory
MODEL_PATH = "yolo"
# initialize minimum probability to filter weak detections along with
# the threshold when applying non-maxima suppression
MIN_CONF = 0.3
NMS_THRESH = 0.3


# To count the total number of people (True/False).
People_Counter = True
# Threading ON/OFF. Please refer 'mylib thread.py'.
Thread = False
# Set the threshold value for total violations limit.
Threshold = 10

# Set url = 0 for webcam.Real time survillieance
url = "http://192.168.137.226:1025/shot.jpg"
# Turn ON/OFF the email alert feature.
SOUND=True
ALERT = False
# Set mail to receive the real-time alerts. E.g., 'xxx@gmail.com'.
MAIL = 'sandiaswi@gmail.com'
# Set if GPU should be used for computations; Otherwise uses the CPU by default.
USE_GPU = True
# Define the max/min safe distance limits (in pixels) between 2 people.
MAX_DISTANCE = 80
MIN_DISTANCE = 50

