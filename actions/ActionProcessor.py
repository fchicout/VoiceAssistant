from actions import Action
from runners.TalkRunner import TalkRunner

import spacy


class ActionProcessor():
        def __str__(self):
            return repr(self) + self.actions

        def extract_verb(self, message):
            nlp = spacy.load("pt")
            doc = nlp(message)
            for token in doc:
                if (token.pos_ == "VERB") and (token.dep_ == "ROOT"):
                    print(token.text)
                    return token.text

        def add_action(self, textMessage):
            cmd = extract_verb(textMessage.lower())
            print(cmd)
            args = textMessage.replace(cmd, '')
            runner = None
            if cmd == "fala":
                runner = TalkRunner()
            action = Action(runner, args)
            self.actions.append(action)

        # def process(self):
        #     try:
        #         if self.actions.count() >= 0:
        #             _thread.start_new_thread(self.actions.popleft().run(), ())
        #     except:
        #         print("Cant' make it run....")

        instance = None

        def __init__(self, action):
            if not ActionProcessor.instance:
                ActionProcessor.instance = ActionProcessor.__ActionProcessor()
            else:
                ActionProcessor.instance.val = action

        def __getattr__(self, name):
            return getattr(self.instance, name)
