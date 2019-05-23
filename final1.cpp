#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;


void leapfrog(float t_inicial, float t_final, string filename);
float E_x(float t);
float E_y(float t);

const double m=7294.29;
const int q=2;
const double dt=0.1;

int main(){
    
  leapfrog(0.0, 10.0, "datos1.dat");
  return 0;
}

float E_x(float t){
return 0;
}

float E_y(float t){
    if (t<3){ 
        return 0;
 }
    if (3<t<7){ 
        return 3;
 }
    if (t>7){ 
        return 0;
 }
}
    
    
    
void leapfrog(float t_inicial, float t_final, string filename){
  float t=t_inicial;
  float v_x=0.0;
  float v_y=1.0;  
  float y=0.0;
  float x=1.0;  
  ofstream outfile;
  outfile.open(filename);
  while(t<t_final){     
    outfile << t << " " << x << " " << y << " " << v_x << " " << v_y << endl;
    v_x = v_x + 0.5 * dt * (q*E_x(t)/m);
    v_y = v_y + 0.5 * dt * (q*E_y(t)/m);  
    x  = x + dt * v_x;
    y  = y + dt * v_y;  
    v_x  = v_x + dt * (q*E_x(t)/m); 
    v_y  = v_y + dt * (q*E_y(t)/m); 
    t = t + dt;
  }
  outfile.close();
}
