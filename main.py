#!/usr/bin/python3

import sys
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


def main():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print('Falaê: ')
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='pt-BR')
                print('You said: {}'.format(text))
                if format(text) == 'L1 na escuta':
                    speech=gTTS("i'm fine dude")
                    speech.save('response.mp3')
                    playsound('response.mp3')
                elif format(text) == 'parou':
                    break
                os.remove('response.mp3')
            except:
                print('Sorry, cant recognize')



if __name__ == '__main__':
    main()
