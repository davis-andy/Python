import cv2 as cv
import os, time, smtplib, imghdr
from email.message import EmailMessage
# pylint: disable=unused-wildcard-import
from settings import *
import speech_recognition as sr

"""
recognize_bing(): Microsoft Bing Speech - https://azure.microsoft.com/en-us/services/cognitive-services/speech-services/
recognize_google(): Google Web Speech - https://wicg.github.io/speech-api/
recognize_google_cloud(): Google Cloud Speech - https://cloud.google.com/speech-to-text
recognize_houndify(): Houndify - https://www.houndify.com/
recognize_ibm(): IBM Speech to Text - https://www.ibm.com/cloud/watson-speech-to-text
recognize_sphinx(): CMU Sphinx - https://cmusphinx.github.io/
recognize_wit(): Wit.ai - https://wit.ai/
"""

"""
for the Pi, use sr.Mircophone.list_microphone_names()
then, mic = sr.Microphone(device_index=3) or index of mic you want to use
"""

# Set up Recognizer and Microphone
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source, duration=1)
    #audio = r.listen_in_background(source)
    audio = r.listen(source)



def get_audio():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Error: " + str(e))
    
    return said.lower()


# pylint: disable=no-member
def send_email(recipient, message):
    msg = EmailMessage()
    msg['From'] = HOTMAIL
    msg['To'] = recipient
    msg['Subject'] = ''

    
    img_data = open(message, 'rb').read()
    msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data))

    SMTP = smtplib.SMTP(HOTMAIL_SMTP, 587)
    SMTP.ehlo()
    SMTP.starttls()
    SMTP.login(HOTMAIL, HOTMAIL_PASSWORD)

    #email_status = EMAIL_SMTP.sendmail(EMAIL, recipient, 'Subject: \n' + msg)
    email_status = SMTP.send_message(msg)

    if email_status != {}:
        print("Error sending email to %s: %s" % (recipient, email_status))

    SMTP.quit()



def take_picture():
    cam = cv.VideoCapture(0)
    _, img = cam.read()

    path = "C:/Users/Andy/Desktop"
    img_file = os.path.join(path, "test.jpg")


    #text = PHONE_NUMBER + ATT_MMS


    while True:
        _, img = cam.read()
        cv.imshow("cam-test", img)
        time.sleep(5)
        cv.imwrite(img_file, img)
        time.sleep(5)
        break

    cam.release()
    cv.destroyAllWindows()

    #time.sleep(2)
    #send_email(text, img_file)
    #time.sleep(5)
    #os.remove(img_file)

def main():

    while True:
        print('Listening')
        heard = get_audio()

        if heard.count(WAKE) > 0:
            heard = get_audio()

            for phrase in PICTURE_STRS:
                if phrase in heard:
                    print('test')
                    take_picture()
                    #turn on LED
                    #take a picture
                    #turn off LED
                    #send picture to app or phone


main()


