from citam_pydraw import *

def on_click():
    print("clicked", mouse.X, mouse.Y)

window = Window(300,300)
mouse = Mouse()

@mouseReleased
def test():
    print("mouseReleased fired!", mouse.X, mouse.Y)

window.show()
