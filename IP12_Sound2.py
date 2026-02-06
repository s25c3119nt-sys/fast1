from citam_pydraw import *

@animation(False)
def draw():
    global pflag
    s = date.second
    #時報（1分毎に音を鳴らす）
    if (int(s)%60 == 0) and pflag:#秒の値が0になった時という条件と最初の再生という条件
        player.play()#音源ファイルを再生する
        pflag = False #毎0秒で1回だけ再生する
        #↑0秒だけど2回目以降はpflagがFalseになるので条件を満たさないから再生されない
    elif (int(s)%60 != 0) and not pflag: 
        pflag = True #0秒台じゃなくなったら次の0秒に向けてpflagをTrueにしておく

if __name__ == "__main__":
    window = Window(400, 400).title("IP12_Sound")
    date = Date()
    player = loadMusic("bell.mp3")
    pflag = True #再生回数を制御するためのフラグ

    draw()
    window.show()
