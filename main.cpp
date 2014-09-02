#include <iostream>

#define TARGET "lifeMan"
#define VERSION "v0.1"

using namespace std;



void usage()
{
	cerr << TARGET	<< " [SWITCHES] <command> [extra params]" << endl;
	cerr << endl;
	cerr << "where SWITCHES:" << endl;
	cerr << "  -opt1" << endl;
	cerr << "  -opt2" << endl;
	cerr << endl;
	cerr << "where command:" << endl;
	cerr << "  log [datetime]\n\tLog an event for a given datetime"  << endl;
	cerr << "  remind [datetime] [-persist=Ndays]\n\tSet a reminder for a given datetime and persist for N days.(Default=99)" << endl;
	cerr << "  show [datetime] [reminder log]\n\tShow log for a given datetime and/or pending reminders." << endl;
	cerr << endl;
}


int main(int argc, char ** argv)
{
	if (argc<2) usage()
	return 0
}
