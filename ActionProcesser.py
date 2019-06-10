from Action import Action


class ActionProcessor():
    class __ActionProcessor:
        def __init__(self, action):
            self.action = action

        def __str__(self):
            return repr(self)+ self.action

    instance = None

    def __init__(self, action):
        if not ActionProcessor.instance:
            ActionProcessor.instance = ActionProcessor.__ActionProcessor(action)
        else:
            ActionProcessor.instance.val = action
    
    def __getattr__(self, name):
        return getattr(self.instance, name)
