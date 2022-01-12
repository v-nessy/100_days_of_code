int numBees = 15; //number of bees

Bees[] bees = new Bees[numBees];

void setup(){
 size(600, 600, P2D); 
 
 for (int i=0; i<bees.length; i++) {
   bees[i] = new Bees(random(width), random(height));
 }
}

void draw(){
  background(90, 155, 205);
  
  for (int i=0; i<bees.length; i++) {
    bees[i].run();
  }
}
