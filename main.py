#!/usr/bin/python3

import sys
from runners.TalkRunner import TalkRunner
import speech_recognition as sr


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
                    greet = TalkRunner("i'm fine dude")
                    greet.run();
                elif format(text) == 'parou':
                    break
                os.remove('response.mp3')
            except:
                print('Sorry, cant recognize')



if __name__ == '__main__':
    main()
