#!/usr/bin/python3

import sys
import os
from runners.TalkRunner import TalkRunner
import speech_recognition as sr


def main():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print('Falaê: ')
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='pt-BR')
                print('You greeted: {}'.format(text))
                if format(text) == 'L1 na escuta':
                    greet = TalkRunner("i'm fine dude, what do you want")
                    greet.run()
                    while True:
                        audio = r.listen(source)
                        try:
                            command = r.recognize_google(audio, language='pt-BR')
                            # Work out actions here
                            print('Your command: {}'.format(command))
                            if format(text) == 'pausa':
                                break
                        except:
                            pass
                elif format(text) == 'parou':
                    break
                os.remove('response.mp3')
            except:
                print('Sorry, cant recognize')


if __name__ == '__main__':
    main()
