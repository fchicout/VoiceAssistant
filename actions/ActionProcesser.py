from actions import Action
from collections import deque

class ActionProcessor():
    class __ActionProcessor:
        def __init__(self):
            self.actions = deque([])

        def __str__(self):
            return repr(self)+ self.actions

        def add_action(self, action):
            self.actions.append(action)

        def process(self):
            self.actions.popleft().run()

    instance = None

    def __init__(self, action):
        if not ActionProcessor.instance:
            ActionProcessor.instance = ActionProcessor.__ActionProcessor()
        else:
            ActionProcessor.instance.val = action
    
    def __getattr__(self, name):
        return getattr(self.instance, name)
