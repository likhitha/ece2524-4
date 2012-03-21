#include <stdlib.h>
#include <iostream>

using namespace std;

int main(int argc, const char* argv[])
{
  unsigned int count = 100;
  if (argc > 1)
    count = atoi(argv[1]);

  for (unsigned int n=0; n<count; ++n)
    {
      cout << n << endl;
    }
}
