// main.cpp: Example main function to demonstrate 'make'
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include<boost/program_options.hpp>

#include "iodat.h"

/* A simple C++ template for a program that accepts command 
 * line options 
 * 
 * Dependencies: Boost.program_options
 */

namespace po = boost::program_options;


using namespace std;
int main(int argc, const char* argv[])
{
    bool verbose=false;
    double N=M_PI;

    po::options_description generic("A simple C++ template program");
    generic.add_options()
	("help,h", "Produce a nice help message")
	("verbose,v", "Be verbose")
	("float,f", po::value<double>(&N)->default_value(M_PI), "a floating point numeric value")
	;
    
    try
    {
	po::variables_map vm;
	po::store(po::parse_command_line(argc, argv, generic), vm);
	po::notify(vm);

	if (vm.count("verbose"))
	    verbose=true;

	if (vm.count("help"))
	{
	    cout << generic << endl; 
	    return EXIT_SUCCESS;
	}

    } catch(std::exception& e) {
	std::cerr << e.what() << std::endl;
	return EXIT_FAILURE;
    }	

    if (verbose)
	cerr << "Initializing ioClass with value " << N << endl;
    ioClass x(N);
    cout << "output is " << x.getval() << endl;
    return EXIT_SUCCESS;
}
