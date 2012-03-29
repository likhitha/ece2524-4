// iodat.cpp: Example implementation file to demonstrate 'make'
#include "iodat.h"
using namespace std;
// default constructor

ioClass::ioClass(const double v) : value(v)
{
}
// member function
double ioClass::getval()
{
    return value;
}
