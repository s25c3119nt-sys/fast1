from citam_pydraw import *

def draw():
    img.show(200, 200)
    Line(200,0,200,400)
    Line(0,200,400,200)

if __name__ == "__main__":
    window = Window(400, 400).title("IP12_Image")
    img = loadImage("kon.png")
    draw()
    window.show()
