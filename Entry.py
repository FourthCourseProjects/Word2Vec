class Entry:
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def __str__(self) -> str:
        return "(" + str(self.input) + ", " + str(self.output) + ")"
