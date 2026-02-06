from citam_pydraw import *

@animation(False)
def draw():
    for i in range(5):
        for j in range(5):
            Rectangle(100*j, 100*i, 100, 100).fill('white')
    mousereleased()

@mouseReleased
def mousereleased():
    print(f"X:{mouse.X}, Y:{mouse.Y}")

if __name__ == "__main__":
    window = Window(500, 500).title("IP09_EX2")
    mouse = Mouse()
    draw()
    window.show()
