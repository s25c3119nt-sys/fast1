from citam_pydraw import *
import random

def draw(levels, size):
    colorMode("HSV")
    for i in range(levels):              # 段数（0〜levels-1）
        for j in range(levels - i):      # 下が広く上が狭い
            x = 200 - ((levels - i) * size / 2) + (j * size)
            y = 400 - (i + 1) * size
            Rectangle(x, y, size, size).fill(color(random.randint(0, 100), 89, 99))

if __name__ == "__main__":
    levels = int(input("段数を入力してください（例: 10）: "))
    size = int(input("□のサイズを入力してください（例: 40）: "))

    window = Window(400, 400).title(f"IP07_Step_{levels}_{size}")
    draw(levels, size)
    window.show()
