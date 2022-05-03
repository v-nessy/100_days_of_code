# Geometric Progression
def setup() :
  size(800, 700)
  smooth()
  
def draw():
  background(253)
  stroke(0) 
  noFill()  
  constantFactor = 1.2 #changing constantFactor adjusts the spacing of the circles
  circleSize = 40 #changing circleSize adjusts the size of all the circles in the for loop
  #^this is how I can grow/shrink the shapes
  #doesn't matter
  
  for i in range(0,20):
      if i == 0: #relocate the smallest circle in the range
        strokeWeight(circleSize/25.0)
        ellipse(width/4,20, circleSize, circleSize)
        circleSize = circleSize * constantFactor 
      else:
        #draws 20 concentric circles of decreasing diameter and decreasing lineWeight
        strokeWeight(circleSize/25.0) 
        ellipse(width/2,height, circleSize, circleSize)
        circleSize = circleSize * constantFactor
        



    
