from djitellopy import tello
from time import sleep
import cv2

me = tello.Tello()
me.connect()
# Get bettery percentage
print(me.get_battery())

# Stream on camera n give frame by frame
me.streamon()

while True:
	img = me.get_frame_read().frame
	img = cv2.resize(img, (360, 240))
	cv2.imshow("Image from Drone", img)
	cv2.waitKey(1)