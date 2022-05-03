c, d = None, None

def setup():
  size(800, 800)
  global c, d
  c= color(random(255), random(255), random(255))
  d= color(random(255), random(255), random(255))


def draw():
  global c, d
  for x in range(width): # loop through every x
    p = lerpColor(c, d, 1.0 * x/width) 
    #changing variables in lerpColor changes either the colour of the gradient or the way the gradient acts
    #changing 1.0 to 1 makes the gradient a single solid colour
    stroke(p)
    line(x, 0, x, height)
    
    # for y in range(height): # loop through every x
    #     p = lerpColor(c, d, 1.0 * y/height) 
    #     stroke(p)
    #     line(y, 0, y, width)

def mousePressed():
  global c, d
  c= color(random(255), random(255), random(255))
  d= color(random(255), random(255), random(255))
