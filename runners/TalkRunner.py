from gtts import gTTS
from playsound import playsound
from runners.Runner import Runner

class TalkRunner(Runner):
    def __init___(self, message2Talk):
        self.message = message2Talk

    def run(self, **args):
        speech=gTTS(self.message)
        speech.save('response.mp3')
        playsound('response.mp3')
        os.remove('response.mp3')