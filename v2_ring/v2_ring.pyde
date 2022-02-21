numRings = 20
currentRing = 0
# Combining week 4 and 5 lecture examples

add_library('sound')
c, d, ch_1, ch_2 = None, None, None, None

rings = [0]*numRings # Declare the array

colour = None

def setup():
  size(300, 300)
  smooth()
  global numRings, colour
  
  global ch_1, ch_2
  ch_1 = SinOsc(this)
  ch_1.play(0,1)
  ch_2 = SinOsc(this)
  ch_2.play(0,1)  
   
  global c, d
  c= color(random(255), random(255), random(255))
  d= color(random(255), random(255), random(255))

  for i in range(numRings): 
    colour = color(random(50,255),random(50,255),random(50,255))
    rings[i] = Ring(0, 0, 0, False, colour) # Create each object

def draw():
  background(40,0,40)
  global numRings, rings
  for i in range(numRings):
    rings[i].grow()
    rings[i].display()

# audio behaviour when clicked
  if mousePressed:
    ch_1.set(400, 1, 0, 0)
    ch_2.set(401, 1, 0, 0)
  else:
    ch_1.set(0, 1, 0, 0)
    ch_2.set(0, 1, 0, 0)  


# Click to create a new Ring
def mousePressed():
  global currentRing, numRings
  rings[currentRing].start(mouseX, mouseY)
  currentRing+=1
  if (currentRing >= numRings):
    currentRing = 0
    
  global c, d
  c= color(random(255), random(255), random(255))
  d= color(random(255), random(255), random(255))
  ch_1.set(400, 1, 0, 0)
  ch_2.set(401, 1, 0, 0)


class Ring(object):
  def __init__(self, x, y, diameter, on, colour):
    self.x = x # x-coordinate
    self.y = y # y-coordinate
    self.diameter = diameter # Diameter of the ring
    self.on = False # Turns the display on and off
    self.colour = colour # initial colour
    
  def start(self, xpos, ypos):
    self.x = xpos;
    self.y = ypos;
    self.on = True;
    self.diameter = 1;

  def grow(self):
    if (self.on == True):
      self.diameter += 1.5
      if (self.diameter > 400):
        self.on = False
  
  def display(self):
    if (self.on == True):
      noFill()
      strokeWeight(4)
      stroke(self.colour) #stroke(255, 153)
      ellipse(self.x, self.y, self.diameter, self.diameter)
