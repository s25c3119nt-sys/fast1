from citam_pydraw import *

def draw():
    for i in range(400):
        hue = i % 100
        Line(i, 0, i, 400).fill(color(hue, 60, 99))

if __name__ == "__main__":
    window = Window(400, 400).title("IP_06_EX")
    colorMode("HSV")
    draw()
    window.show()
