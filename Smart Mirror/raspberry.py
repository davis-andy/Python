import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from settings import GPIO_PIN, IMG_LOCATION

class Raspberry:
    camera = PiCamera()
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_PIN, GPIO.OUT)


    def led_pic(self, on_off):
        GPIO.output(GPIO_PIN, on_off)

    def take_picture(self):
        # self.camera.resolution()  # max = 2592 x 1944, min = 64 x 64, default is set to monitor
        self.camera.framerate = 15
        #self.camera.start_preview(alpha=200)
        #time.sleep(2)
        self.camera.capture(IMG_LOCATION)
        #self.camera.stop_preview()