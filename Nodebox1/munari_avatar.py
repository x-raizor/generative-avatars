
# Avatar Generator based on Bruno Munari's faces

from math import sqrt
supershape = ximport("supershape")
colors = ximport("colors")
svg = ximport("svg")


def drawpaths(paths=[], x=0, y=0, rotate=0, scale=1.0, origin=(0.5,0.5)):
    ''' Draws a group of paths that rotate and scale from the given origin.
    '''
    _ctx.transform(CORNER)
    _ctx.push()
    _ctx.translate(x, y)
    _ctx.rotate(rotate)
    _ctx.scale(scale)
    (x, y), (w, h) = bounds(paths)
    _ctx.translate((-x-w)*origin[0], (-y-h)*origin[1])
    for path in paths:
       # Use copies of the paths that adhere to the transformations.
       _ctx.drawpath(path.copy())
    _ctx.pop()


def bounds(paths=[]):
  ''' Returns (x, y), (width, height) bounds for a group of paths.
  '''
  if len(paths) == 0: 
    return (0,0), (0,0)
  l = t = float("inf")
  r = b = float("-inf")
  for path in paths:
    (x, y), (w, h) = path.bounds
    l = min(l, x)
    t = min(t, y)
    r = max(r, x+w)
    b = max(b, y+h)
  return (l, t), (r-l, b-t)
  

def draw_svgshape(index = None): 
    if not index:
        filename = choice(files_list)
    else:
        filename = faces_path + "face_" + "%05d" % (index) +".svg"
    data = open(filename).read()
    paths = svg.parse(data, cached=True)
    origin, (w, h) = bounds(paths)
    _scale = _size/sqrt(2)/max(w, h)
    _x = WIDTH/2 + w/2*_scale 
    _y = HEIGHT/2 + h/2*_scale
    _x += 250
    _y -= 800 
    push()
    drawpaths(paths, x = _x, y = _y, scale = _scale, rotate = 0)
    pop()


def draw_supershape():
    x = y = WIDTH/2
    w = h = _size/sqrt(2)/2
    drawpath(supershape.path(
            x, y, w, h, 
            random(2, 20), random(0.3, 20), random(0.3, 20), random(0.3, 20),
            points = 100, percentage = 1.0, range = 3.14159*2
    ))
    


def bgfill():
    background(colors.hex("#FFDB80"))
    push()
    fill(255)
    draw_supershape()
    pop()
    

def make_avatar(index = None):
    bgfill()
    fill(0)
    draw_svgshape(index)
    

_size = 512
faces_path = "/Users/andrew/Dropbox/Python/+nodebox/+avatars/munari-svg/"
output_path = "/Users/andrew/Dropbox/Python/+nodebox/+avatars/avatars/type3/"
files_list = files(faces_path + "*.svg")

size(_size, _size)

canvas.clear()
make_avatar()
    

