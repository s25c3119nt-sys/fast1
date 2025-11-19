from citam_pydraw import *

clicked = [
    [False, False],
    [False, False]
]

colors = [
    [10, 40],
    [60, 90]
]

@animation(False)
def draw():
    for i in range(2):
        for j in range(2):
            x = 200 * j
            y = 200 * i
            if clicked[i][j]:
                Rectangle(x, y, 200, 200).fill(color(colors[i][j], 99, 99))
            else:
                Rectangle(x, y, 200, 200).fill("white")
    mousereleased()    


@mouseReleased
def mousereleased():
    mx = mouse.X
    my = mouse.Y
    print(f"X:{mx}, Y:{my}")

    if 0 <= mx <= 400 and 0 <= my <= 400:
        j = mx // 200
        i = my // 200


        clicked[i][j] = not clicked[i][j]

        draw()


if __name__ == "__main__":
    window = Window(400, 400).title("IP09_EX1")
    mouse = Mouse()
    colorMode("HSV")
    draw()
    window.show()