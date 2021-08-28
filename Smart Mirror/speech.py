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
class Speech():
    """
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)
        #audio = r.listen_in_background(source)
        audio = r.listen(source)
    """


    def get_audio(self):
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
