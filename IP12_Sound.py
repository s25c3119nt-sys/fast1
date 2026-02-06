from citam_pydraw import *

def play_music():
    player.play()

if __name__ == "__main__":
    window = Window(400, 400).title("IP12_Sound")
    player = loadMusic("bell.mp3")
    play_music()
    window.show()
