import speech_recognition as sr
from gtts import gTTS
from transformers import pipeline, set_seed


from config import Config as config


def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

# Usage
text = "Hello Virgilio, suck my dick."
filename = "virgilio.mp3"
text_to_speech(text, filename)
