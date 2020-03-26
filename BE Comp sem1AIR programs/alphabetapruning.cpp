#include<iostream>
using namespace std;
const int MAX= -1000; //alpha
const int MIN= 1000;//beta
int minimax(int depth, int nodeIndex, 
            bool maximizingPlayer, 
            int values[], int alpha,  
            int beta) 
{ 
      
    // Terminating condition. i.e  
    // leaf node is reached 
    if (depth == 3) 
        return values[nodeIndex]; 

  if (maximizingPlayer)  //alpha calculation maximizingplayer=false
    { 
        
        // Recur for left and  
        // right children 
        for (int i = 0; i < 2; i++) 
        { 
              
            int val = minimax(depth + 1, nodeIndex * 2 + i,  
                              false, values, alpha, beta); 
            alpha = max(alpha, val); 
  
            // Alpha Beta Pruning 
            if (beta <= alpha) 
                break; 
        } 
        return alpha; 
    }


 else                    //Beta calculation maximizingplayer=false
    { 
  
        // Recur for left and 
        // right children 
        for (int i = 0; i < 2; i++) 
        { 
            int val = minimax(depth + 1, nodeIndex * 2 + i, 
                              true, values, alpha, beta); 
	    beta=min(beta,val);
  
            // Alpha Beta Pruning 
            if (beta <= alpha) 
                break; 
        } 
        return beta; 
    } 



}

int main() 
{ 
    int values[8] = { 2,3,5,9,0,1,7,5}; 
    cout <<"The optimal value is : "<< minimax(0, 0, true, values, MAX, MIN);; 
    return 0; 
}

########################################################################## 

'''
values = [3, 5, 6, 9, 1, 2, 0, -1] 
	print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX)) 
	
##########################################################################################
output:
administrator@112C-11:~$ cd Desktop
administrator@112C-11:~/Desktop$ cd AIR
administrator@112C-11:~/Desktop/AIR$ python alphabeta.py
('The optimal value is :', 5)
'''