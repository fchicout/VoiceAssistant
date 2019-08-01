
import os
from gtts import gTTS
from playsound import playsound
from runners.Runner import Runner


class CameraRunner(Runner):
    def __init___(self, option):
        # option can be save or talk
        self.option = option

    def run(self, **args):
        if self.option == "save":
            speech = gTTS("Founding faces")
            speech.save('response.mp3')
            playsound('response.mp3')
            os.remove('response.mp3')
