#include <stdlib.h>
#include <iostream>

using namespace std;

int main (int argc, const char* argv[])
{
  for (int i=0; i<argc; i++)
    cout << "argv[" << i << "]=" << argv[i] << endl;

  return EXIT_SUCCESS;
}
