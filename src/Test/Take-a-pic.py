# This code is directly from the provided repository in the 
# README file, from the module, djitellopy

import cv2
from djitellopy import Tello
import time

drone = Tello()
drone.connect()

drone.streamon()
frame_read = drone.get_frame_read()

drone.takeoff()
cv2.imwrite(f"{time.time()}.jpg", frame_read.frame)

drone.land()