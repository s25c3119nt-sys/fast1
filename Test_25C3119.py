from citam_pydraw import *


window = Window()
window.title("IP_02_EX")
window.size(400,400)
window.background(color(255,255,255))
point = Point(100,100,5)
line = Line(150,150,180,100,5)

triangle = Triangle(200,200,250,250,150,250)
triangle.outlineWidth(5)
triangle.noFill()

rectangle = Rectangle(5, 300, 50, 80)
rectangle.outlineFill(color(255,0,0))
rectangle.outlineWidth(5)
rectangle.noFill()

quad = Quad(100,300,150,270,200,300,150,350)
quad.outlineFill(color(255,0,0))
quad.outlineWidth(5)
quad.noFill()

ellipse = Ellipse(300, 100, 80, 50)
ellipse.outlineFill(color(255,0,0))
ellipse.outlineWidth(5)
ellipse.fill(color(0,0,255))

arc = Arc(100,100,180,180,90,90)
arc.noOutline()
arc.fill(color(0,255,0))

window.show()