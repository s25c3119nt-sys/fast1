from citam_pydraw import *

def draw(win):
    w = win.width
    h = win.height
    rows = 10
    cols = 10
    spacing_x = w / cols
    spacing_y = h / rows
    for i in range(rows):
        for j in range(cols):
            x = spacing_x * j + spacing_x / 2
            y = spacing_y * i + spacing_y / 2
            Ellipse(x, y, spacing_x, spacing_y).noOutline().fill(color(10*j, 10+10*i, 99))

if __name__ == "__main__":
    window = Window(600, 400).title("IP_06_Loop09_scaled")
    colorMode("HSV")
    draw(window)
    window.show()

