from runners.Runner import Runner

class Action(Runner):

    def __init__(self, command, runner, args):
        self.command = command
        self.runner = runner
        self.args = args

    def run(self, **args):
        raise NotImplementedError
