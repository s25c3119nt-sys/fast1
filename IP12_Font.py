from citam_pydraw import *

def draw():
    text1 = Text(u"はろー", 200, 75)
    text1.font("", 48)#好きなフォントを入れる
    text2 = Text(u"ちばてっく", 200, 125)
    text2.font("", 48)#好きなフォントを入れる

if __name__ == "__main__":
    window = Window(400, 200).title("IP12_Font")
    draw()
    window.show()
