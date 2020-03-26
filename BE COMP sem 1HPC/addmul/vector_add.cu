#include "stdio.h"
#include<cuda.h>
#define SOA 512

__global__ void vector_add(int *a,int *b,int *c){
	int id= threadIdx.x;
	c[id]=a[id]+b[id];
}

int main(void){

	int i;
	int *a,*b,*c;
	int *da,*db,*dc;
	int size=sizeof(int) * SOA;

	a = (int *)malloc(size);
	b = (int *)malloc(size);
	c = (int *)malloc(size);

	for(i=0;i<SOA;i++){
		a[i]= i;
		b[i]= i+1;
	}
	
	cudaMalloc((void**)&da,size);
	cudaMalloc((void**)&db,size);
	cudaMalloc((void**)&dc,size);

	cudaMemcpy(da,a,size,cudaMemcpyHostToDevice);
	cudaMemcpy(db,b,size,cudaMemcpyHostToDevice);
	
	vector_add<<<1,SOA>>>(da,db,dc);

	cudaMemcpy(c,dc,size,cudaMemcpyDeviceToHost);

	printf("Addition : ");
	for(i=0; i<SOA; i++)
	{
		printf("%d\n",c[i]);
	}
	cudaFree(da);
	cudaFree(db);
	cudaFree(dc);
	return 0;
	

}
	
