/* *
 * Copyright 1993-2012 NVIDIA Corporation.  All rights reserved.
 *
 * Please refer to the NVIDIA end user license agreement (EULA) associated
 * with this source code for terms and conditions that govern your use of
 * this software. Any use, reproduction, disclosure, or distribution of
 * this software and related documentation outside the terms of the EULA
 * is strictly prohibited.
 */
#include <stdio.h>
#include <stdlib.h>

static const int WORK_SIZE = 10;

/**
 * This macro checks return value of the CUDA runtime call and exits
 * the application if the call failed.
 */
 /*
define CUDA_CHECK_RETURN(value) 
{											
	cudaError_t _m_cudaStat = value;										
	if (_m_cudaStat != cudaSuccess) {										
		fprintf(stderr, "Error %s at line %d in file %s\n",					
				cudaGetErrorString(_m_cudaStat), __LINE__, __FILE__);
		exit(1);															
	} }
*/
__global__ void sort(int *a,int i,int n)
{
	int tid = threadIdx.x;
	int p;
	int temp;
	if(i%2==0)
	{
		p=tid*2;

		if(a[p]>a[p+1])
		{
			temp = a[p];
			a[p] = a[p+1];
			a[p+1] =temp;
		}
	}
	else
	{
		p=tid*2+1;

		if(p<n-1)
		{
			if(a[p]>a[p+1])
			{
				temp = a[p];
				a[p] = a[p+1];
				a[p+1] =temp;
			}
		}
	}
}

/**
 * Host function that prepares data array and passes it to the CUDA kernel.
 */
int main(void)
{
	int a[WORK_SIZE];
	int i;
	int *da;

	cudaMalloc((void**) &da, sizeof(int) * WORK_SIZE);

	for(i=0;i<WORK_SIZE;i++)
	{
		printf("%d:",i);
		scanf("%d",&a[i]);
	}


	cudaMemcpy(da, a, sizeof(int) * WORK_SIZE, cudaMemcpyHostToDevice);

	for(i=0;i<WORK_SIZE;i++)
	{
		sort<<<1,WORK_SIZE/2>>>(da,i,WORK_SIZE);
	}

	cudaThreadSynchronize();	// Wait for the GPU launched work to complete
	cudaGetLastError();

	cudaMemcpy(a, da, sizeof(int) * WORK_SIZE, cudaMemcpyDeviceToHost);

	for(i=0;i<WORK_SIZE;i++)
	{
		printf("%d\t",a[i]);

	}

	printf("\n");

	cudaFree((void*) da);


	return 0;
}




