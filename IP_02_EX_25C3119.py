from citam_pydraw import *


window = Window()
window.title("IP_02_EX")
window.size(400,400)
window.background(color(255,255,255))

#輪郭
ellipse = Ellipse(200, 200, 300, 300)
ellipse.outlineWidth(5)
ellipse.noFill()

#左目
ellipse = Ellipse(160, 160, 40, 80)
ellipse.outlineWidth(5)
ellipse.noFill()

#右目
ellipse = Ellipse(240, 160, 40, 80)
ellipse.outlineWidth(5)
ellipse.noFill()

#左眉
arc= Arc(160, 160, 100, 150, 50, 130)
arc.outlineStyle('arc')
arc.outlineWidth(5)
arc.noFill()

#右眉
arc= Arc(240, 160, 100, 150, 0, 130)
arc.outlineStyle('arc')
arc.outlineWidth(5)
arc.noFill()

#鼻
ellipse = Ellipse(200, 230, 90, 90)
ellipse.outlineWidth(5)
ellipse.noFill()

#左頬
ellipse = Ellipse(110, 230, 95, 95)
ellipse.outlineWidth(5)
ellipse.noFill()

#右頬
ellipse = Ellipse(290, 230, 95, 95)
ellipse.outlineWidth(5)
ellipse.noFill()

#口
arc = Arc(200, 280, 120, 60, 200, 140)
arc.outlineStyle('arc')
arc.outlineWidth(5)
arc.noFill()


window.show()