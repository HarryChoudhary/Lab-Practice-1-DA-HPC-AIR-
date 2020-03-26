Vector addition program

#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>

#define n 512

__global__ void bmk_add(int *a, int *b, int *result)
{
  int i = threadIdx.x;
  result[i] = a[i] + b[i];
}

int main()
{
  int num_blocks = 1, num_threads = n;

  int *a, *b, *c;
  int *dev_a, *dev_b, *dev_c;

  int size = n * sizeof(int);

  a = (int*)malloc(size);
  b = (int*)malloc(size);
  c = (int*)malloc(size);

  cudaMalloc((void**)&dev_a,size);
  cudaMalloc((void**)&dev_b,size);
  cudaMalloc((void**)&dev_c,size);

  for(int i = 0;i<n;i++)
  {
    //a[i] = rand()%1024;
    //b[i] = rand()%1024;
    a[i] = i;
    b[i] = i;
  }

  cudaMemcpy(dev_a,a,size,cudaMemcpyHostToDevice);
  cudaMemcpy(dev_b,b,size,cudaMemcpyHostToDevice);

  bmk_add <<<num_blocks, num_threads>>>(dev_a,dev_b,dev_c);

  cudaMemcpy(c,dev_c,size,cudaMemcpyDeviceToHost);

  for(int i = 0;i<n;i++)
    printf("%d  ",c[i]);
    
    printf("\n");
  cudaFree(dev_a);
  cudaFree(dev_b);
  cudaFree(dev_c);

  return 0;
}

######################################################################################################################################################################################################
Multiplication program

#include<stdio.h>
#define Width 4
#define TILE_WIDTH 2
__global__ void mat_mul(int *a, int *b,int *ab, int width)
{
  // shorthand
  int tx = threadIdx.x, ty = threadIdx.y;
  int bx = blockIdx.x, by = blockIdx.y;
  // allocate tiles in __shared__ memory
  __shared__ int s_a[TILE_WIDTH][TILE_WIDTH];
  __shared__ int s_b[TILE_WIDTH][TILE_WIDTH];
  // calculate the row & col index
  int row = by*blockDim.y + ty;
  int col = bx*blockDim.x + tx;
  int result = 0;

  // loop over the tiles of the input in phases
  for(int p = 0; p < width/TILE_WIDTH; ++p)
  {
    // collaboratively load tiles into __shared__
    s_a[ty][tx] = a[row*width + (p*TILE_WIDTH + tx)];
    s_b[ty][tx] = b[(p*TILE_WIDTH + ty)*width + col];
    __syncthreads();
    // dot product between row of s_a and col of s_b
    for(int k = 0; k < TILE_WIDTH; ++k)
    result += s_a[ty][k] * s_b[k][tx];
    __syncthreads();
  }
  ab[row*width+col] = result;
}


int main()
{
    int mat_size=Width*Width*sizeof(int); //Calculate memory size required for float matrix
    int tot_elements=Width*Width;
    int *M,*N,*P,*ptr;  // Host matrix pointers
  int a=0,x=1;
  int i=0;
  int *Md,*Nd,*Pd;    //Matrix Pointer on device memoryi.e GPU
  //int size=Width*Width*sizeof(int);
  

  M=(int*)malloc(mat_size);   //Allocate memory on host for matrix
  N=(int*)malloc(mat_size);
  P=(int*)malloc(mat_size);
  //P_CPU=(int*)malloc(mat_size);
  ptr=M;
  printf("\nGenarating random elements for matrix");
  for(i=0;i<tot_elements;i++)
  { //a=(rand()%10);    //Generates random no. in 0 to 10 range
    //*ptr=a;
    *ptr=x++;
    ptr++;
  }
  ptr=N;
  for(i=0;i<tot_elements;i++)
  {
    //a=(rand()%10);
    *ptr=x--;
    ptr++;
  }
  printf("Matrix A=\n ");
  for(int i=0;i<Width*Width;i++)
  { if(i%(Width)==0){
      printf("\n");
    }
    printf("%d ",M[i]);
  }
printf("Matrix B=\n ");
  for(int i=0;i<Width*Width;i++)
  { if(i%(Width)==0){
      printf("\n");
    }
    printf("%d ",N[i]);
  }
  cudaMalloc((void**)&Md,mat_size);   //Allocate memory on device global memory
  cudaMemcpy(Md,M,mat_size,cudaMemcpyHostToDevice); //Copy matrix data from host to device memory
  cudaMalloc((void**)&Nd,mat_size);
  cudaMemcpy(Nd,N,mat_size,cudaMemcpyHostToDevice);
  cudaMalloc((void**)&Pd,mat_size);

  dim3 dimGrid(TILE_WIDTH,TILE_WIDTH);  //Variable for threads arrangement in a block.
  dim3 dimBlock(Width/TILE_WIDTH,Width/TILE_WIDTH);   //Variable for blocks arrangement in a grid.  

  mat_mul<<<dimGrid,dimBlock>>>(Md,Nd,Pd,Width);  //Kernel invocation with grid and block specification in angle brackets
  

  cudaMemcpy(P,Pd,mat_size,cudaMemcpyDeviceToHost); //Copy resultant matrix from device to host
  //display the resultant matrix  
printf("Product=\n ");
  for(int i=0;i<Width*Width;i++)
  { if(i%(Width)==0){
      printf("\n");
    }
    printf("%d ",P[i]);
  }
  //Free device memory
  cudaFree(Md);
  cudaFree(Nd);
  cudaFree(Pd);
free(M);
free(N);
free(P);
}

