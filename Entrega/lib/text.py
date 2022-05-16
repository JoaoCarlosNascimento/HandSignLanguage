class word:
    def __init__(self, text, video):
        self.text = text
        self.video = video
    def on_hover(self):
        pass

class phrase:
    def __init__(self, words):
        self.phrase = words
    def display(self):
        pass
