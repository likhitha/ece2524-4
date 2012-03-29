//This is file sqrt.cpp
//It will be used to demonstrate standard I/O
#include <stdlib.h>
#include <math.h>
#include <iostream>
using namespace std;

int main()
{
  double x;
  while (cin >> x)
    {
      if (x < 0.0)
	cerr << "sqrt: input " << x << " is negative!" << endl;
      else
	cout << "square root of " << x << " is " << sqrt(x) << endl;
    }
  return EXIT_SUCCESS;
}
  
