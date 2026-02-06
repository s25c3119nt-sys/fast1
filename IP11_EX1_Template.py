#ひーろーすたんぷ
#マウスクリックしたところにヒーローのスタンプをする
#英文字のa,b,c（ヒーローのサイズ変更:a=1倍(初期値), b=2倍, c=0.5倍）
#英文字のd,e,f（ヒーローの色の変更:d色1(初期値)，e色2，f色3）
#英文字のz（キャンパスのクリア）
#ヒーローのサイズや色などはグローバル変数を用いる
#ヒーローの描画はユーザ定義関数（ヒーロー関数）で行う
#ヒーロー関数は引数として 描画座標x, 描画座標y をうけとる
from citam_pydraw import *

@animation(False)
def draw():
    keypressed()
    mousereleased()
    #draw関数はこの2行以外は不要

@keyPressed
def keypressed():
    #a,b,c,d,e,f,zが押された時のそれぞれの処理を記入
    #a,b,cが押されたらヒーローの顔のサイズの変数の値の変更
    #d,e,fが押されたらヒーローの色のリストのインデックスの変数の値を変更
    #zが押されたら clear() を呼び出す

@mouseReleased
def mousereleased():
    #クリックされたらヒーローの顔を描画する関数（drawHeroFace）を呼び出す
    #呼び出す際に引数で mouse.X, mouse.Y を渡す

def drawHeroFace(cx, cy):
    #ヒーローの顔を描画する関数
    #引数で与えられたcx, cyを中心として各パーツを描画
    #ヒーローの顔のサイズのグローバル変数(heroSize)で大きさを変更（掛け算を使うと楽）
    #描画時にヒーローの色のグローバル変数のリスト(heroColor)から色を取得
    #色のパターンはインデックスを指定するグローバル変数heroColorIndexから取得


if __name__ == "__main__":
    window = Window(700, 700).title("IP11_EX1")
    
    keyboard = KeyBoard() # キーボードを使えるようにする
    mouse = Mouse() # マウスを使えるようにする

    heroSize = 1.0 #ヒーローのサイズの変数
    #ヒーローの色のリスト：顔の色，鼻の色，頬の色，目の色，テカリの色
    #各パターンの色の値を最内の[]に定義していく
    heroColor = [[[],[],[],[],[]], #パターン0
                 [[],[],[],[],[]], #パターン1
                 [[],[],[],[],[]]] #パターン2
    heroColorIndex = 0 #ヒーローの色のリストのインデックス（パターン）を指定する変数

    draw()
    window.show()
