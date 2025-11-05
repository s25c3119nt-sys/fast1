from citam_pydraw import *

def draw():
    colorMode("HSV")
    for i in range(10):              # 段（0〜9）
        for j in range(10 - i):      # 下が広く、上ほど短い
            x = j * 40          # 左詰め配置
            y = 360 - i * 40         # 下から上へ
            Rectangle(x, y, 40, 40).fill(color(10 *(9 - i), 99, 99))

if __name__ == "__main__":
    window = Window(400, 400).title("IP_07_EX01_25C3119")
    draw()
    window.show()


