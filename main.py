#!/usr/bin/python3

import sys
import os
from runners.TalkRunner import TalkRunner
from actions.ActionProcessor import ActionProcessor
import speech_recognition as sr


def main():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print('Falaê: ')
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)
            try:
                # Brazilian Portuguese Recognition
                text = r.recognize_google(audio, language='pt-BR')
                # text = r.recognize_google(audio) # English recognition
                print(format(text))
                if 'computador' in format(text):
                    print(format(text))
                    # Send command to be processed
                elif "pare" in format(text):
                    print("Done")
                    break
            except:
                print('Sorry, cant recognize')


if __name__ == '__main__':
    main()
