from gtts import gTTS
from playsound import playsound
from Runner import Runner

class TalkRunner(Runner):
    def __init___(self, message2Talk):
        speech=gTTS("i'm fine")
        speech.save('response.mp3')
        playsound('response.mp3')
        os.remove('response.mp3')