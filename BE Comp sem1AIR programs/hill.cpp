#include <iostream>
using namespace std;

int calcCost (int ArrayOfCities[], const int NUM_CITIES) 
{
	int c = 0;
	for (int i = 0; i < NUM_CITIES; ++i)
	{
		for (int j = i + 1; j < NUM_CITIES; ++j)
		{
			if (ArrayOfCities[j] < ArrayOfCities[i])
			{
				c++;
				cout<<" c is"<<c;
			}
		}
	}
	return c;
}

void SwapElements (int ArrayOfCities[], int i, int j)
{
	int temp = ArrayOfCities[i];
	ArrayOfCities[i] = ArrayOfCities[j];
	ArrayOfCities[j] = temp;
}

int main()
{
	const int CITIES = 8;
	int iIndex = 1;
	int ArrayOfCities[CITIES];

	for (int i = 0; i < CITIES; ++i)
	{
		cout << "Enter distance for city " << iIndex << endl;
		cin >> ArrayOfCities[i];
		++iIndex;
	}

	int bestCost = calcCost(ArrayOfCities, CITIES);
	cout<<bestCost;
	int iNewCost = 0, iSwaps = 0;
	while (bestCost > 0) 
	{
		for (int i = 0; i < CITIES - 1; ++i)
		{
			SwapElements(ArrayOfCities, i, i + 1);
			iNewCost = calcCost(ArrayOfCities, CITIES);
			if (bestCost > iNewCost)
			{
				++iSwaps;
				cout << "Performing Swap: " << iSwaps << endl;
				for (int i = 0; i < CITIES; ++i)
				{
					cout << ArrayOfCities[i] << "->";
				}

				cout << "\n";
				bestCost = iNewCost;
			}
			else
			{
				SwapElements(ArrayOfCities, i, i + 1);
			}
		}
	}
	
	cout << "\nFinal Route: \n";
	for (int i = 0; i < CITIES; i++)
	{
		cout << ArrayOfCities[i] << endl;
	}
}




'''
#############################################################################
output:
administrator@112C-11:~$ cd Desktop
administrator@112C-11:~/Desktop$ cd AIR
administrator@112C-11:~/Desktop/AIR$ g++ hill.cpp
administrator@112C-11:~/Desktop/AIR$ ./a.out
Enter distance for city 1
6
Enter distance for city 2
5
Enter distance for city 3
14
Enter distance for city 4
7
Enter distance for city 5
9
Enter distance for city 6
3
Performing Swap: 1
5->6->14->7->9->3->
Performing Swap: 2
5->6->7->14->9->3->
Performing Swap: 3
5->6->7->9->14->3->
Performing Swap: 4
5->6->7->9->3->14->
Performing Swap: 5
5->6->7->3->9->14->
Performing Swap: 6
5->6->3->7->9->14->
Performing Swap: 7
5->3->6->7->9->14->
Performing Swap: 8
3->5->6->7->9->14->

Final Route: 
3
5
6
7
9
14
administrator@112C-11:~/Desktop/AIR$ 


'''
