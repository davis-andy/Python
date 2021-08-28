from speech import Speech
from raspberry import Raspberry
from send_photo import SendPhoto
# pylint: disable=unused-wildcard-import
from settings import *


# Set up classes
rasp = Raspberry()
speak = Speech()
send = SendPhoto()


while True:
    heard = speak.get_audio()
    print('Listening')

    if heard.count(WAKE) > 0:
        heard = speak.get_audio()

        for phrase in PICTURE_STRS:
            if phrase in heard:
                #turn on LED
                rasp.led_pic(True)
                #take a picture
                rasp.take_picture()
                #turn off LED
                rasp.led_pic(False)
                #send picture to app or phone
                send.send_email(PHONE_NUMBER + ATT_MMS, IMG_LOCATION)
