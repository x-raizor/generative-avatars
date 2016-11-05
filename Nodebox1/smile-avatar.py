import os
from AppKit import *
supershape = ximport("supershape")
colors = ximport("colors")


def bgfill():
    background(255)
    push()
    hue = random()
    r = colors.range(
        h=(0.0, 0.6),
        s=(0.35, 0.4),
        b=(0.6, 0.8)
    )
    transform(CORNER)
    rotate(90*random())
    for i in range(HEIGHT/10):
        fill(choice(r))
        rect(-WIDTH, i * 64, WIDTH * 2, 68)
    pop()

    
def smile():
    push()
    transform(CENTER)
    rotate(-90)
    fill(255)    
    eyes = [":", "|", "8", ";", "'"]
    nose = [u"-", u"—", u"·"]
    mouth = ["]", ")", "/"]
    face_figure = choice(eyes) + choice(nose) + choice(mouth)

    fontManager = NSFontManager.sharedFontManager()
    fonts = fontManager.availableFonts()
    font_name = fonts[int(len(fonts) * random())]
    font(font_name, _fontsize)
    
    __fontsize = _fontsize
    w, h = textmetrics(face_figure)
    while h > _fontsize:
        __fontsize -= 5
        font(font_name, __fontsize)
        w, h = textmetrics(face_figure)    
    
    w, h = textmetrics(face_figure)
    p = textpath(face_figure, _size/2 - w/2, _size/2 - h/2)
    bounds =  p._nsBezierPath.bounds()
    p = textpath(face_figure, _size/2 - bounds[1][0]/2, _size/2 + bounds[1][1]/2)
    drawpath(p)
    pop()
        

_size = 512
_fontsize = _size * 0.65
size(_size, _size)

bgfill()
smile()
    
    
    