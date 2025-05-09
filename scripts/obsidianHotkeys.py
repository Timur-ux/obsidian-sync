import keyboard
import time

isEngLayout = True

class Abbreviation:
    def __init__(self, word: str, action, condition):
        self.word = word
        self.action = action
        self.condition = condition
        self.pos = 0

    def onPress(self, letter):
        if letter == self.word[self.pos]:
            self.pos += 1
            print(letter, self.word, self.pos, self.condition())
            if self.pos == len(self.word):
                self.pos = 0
                if self.condition():
                    self.action()
        else:
            self.pos = 0

def send_word(word: str):
    for c in word:
        keyboard.send(c)

def change_layout(hotkey="shift+alt"):
    global isEngLayout
    isEngLayout = not isEngLayout
    keyboard.send(hotkey)
    print("layout changed")

def change_word(word: str, need_change_layout=True):
    for c in word:
        keyboard.send("backspace")
    if need_change_layout:
        change_layout()
    send_word(word)

def on_layout_changed():
    global isEngLayout
    isEngLayout = not isEngLayout
    print("layout changed")

def on_word_action(word, action):
    def wrapper():
        for c in word:
            keyboard.send("backspace")
        action()
    return wrapper

keyboard.add_hotkey("alt+shift", on_layout_changed)
def send_multiple(keys:list, delay: float = .0):
    for key in keys:
        keyboard.send(key)
        time.sleep(delay)

def on_math_exit():
    send_multiple(["ctrl+f", "shift+4", "esc", "left", "tab"])
    change_layout()

abbreviations = [
        Abbreviation("mk", lambda: change_word("mk"), lambda: not isEngLayout),
        Abbreviation("dm", lambda: change_word("dm"), lambda: not isEngLayout),
        Abbreviation("jk", on_word_action("jk", on_math_exit), lambda: isEngLayout),
        ]

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        for abbr in abbreviations:
            abbr.onPress(event.name)

