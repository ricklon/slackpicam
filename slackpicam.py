from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)

camera.capture('foobar.jpg')
