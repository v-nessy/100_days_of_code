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
  
  for i in range(0,20):
    #draws 20 concentric circles of decreasing diameter and decreasing lineWeight
    strokeWeight(circleSize/25.0) 
    ellipse(width/2,height, circleSize, circleSize)
    circleSize = circleSize * constantFactor 
    



    
