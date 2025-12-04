from citam_pydraw import *


heroSize = 1.0
heroColorIndex = 0

heroColor = [
    [color(255,220,180), color(255,180,160), color(255,200,180), color(0,0,0), color(255,255,255)],
    [color(200,230,255), color(180,200,255), color(160,180,255), color(0,0,50),  color(255,255,255)],
    [color(255,255,0), color(255,200,150), color(255,170,140), color(20,20,20), color(255,255,255)]
]


@animation(False)
def draw():
    keypressed()
    mousereleased() 





@mouseReleased
def mousereleased():
    drawHeroFace(mouse.X, mouse.Y)


def drawHeroFace(cx, cy):
    global heroSize, heroColorIndex
    s = heroSize
    col = heroColor[heroColorIndex]

    Ellipse(cx, cy, 300*s, 300*s).fill(col[0]).outlineWidth(5)

    Ellipse(cx - 40*s, cy - 40*s, 40*s, 80*s).fill(col[3]).outlineWidth(5)
    Ellipse(cx + 40*s, cy - 40*s, 40*s, 80*s).fill(col[3]).outlineWidth(5)

    Arc(cx - 40*s, cy - 40*s, 100*s, 150*s, 50, 130).outlineStyle("arc").outlineWidth(5).noFill()
    Arc(cx + 40*s, cy - 40*s, 100*s, 150*s, 0, 130).outlineStyle("arc").outlineWidth(5).noFill()

    Ellipse(cx, cy + 30*s, 90*s, 90*s).fill(col[1]).outlineWidth(5)

    Ellipse(cx - 90*s, cy + 30*s, 95*s, 95*s).fill(col[2]).outlineWidth(5)
    Ellipse(cx + 90*s, cy + 30*s, 95*s, 95*s).fill(col[2]).outlineWidth(5)

    Arc(cx, cy + 80*s, 120*s, 60*s, 200, 140).outlineStyle("arc").outlineWidth(5).noFill()

@keyPressed
def keypressed():
    global heroSize, heroColorIndex

    if keyboard.key == "a":
        heroSize = 1.0
    elif keyboard.key == "b":
        heroSize = 2.0
    elif keyboard.key == "c":
        heroSize = 0.5

    elif keyboard.key == "d":
        heroColorIndex = 0
    elif keyboard.key == "e":
        heroColorIndex = 1
    elif keyboard.key == "f":
        heroColorIndex = 2

    elif keyboard.key == "z":
        clear()

if __name__ == "__main__":
    window = Window(700, 700).title("IP11_EX1")
    
    keyboard = KeyBoard()
    mouse = Mouse()

    draw()
    window.show()
