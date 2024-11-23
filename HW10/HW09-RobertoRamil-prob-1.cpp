#include <iostream>
#include <cmath>
#include <cstdlib>
#include <iomanip>

using std::cout;
using std::cin;
using std::endl;

int main(int argc, const char** argv){

    cout << "Printing the Square root of -1: " << sqrt(-1)<< endl;
    cout << "it outputs nan which is 'not a number'" << endl;
    cout << "Printing the cos^-1(2): " << acos(2.0) << "\nSame thing here it does not exist"<< endl;

    cout << "Printing log(0.0): " << log(0.0) <<"\nThis is -inf which is the smallests negative number the computer can show." <<  endl;

    return 0;
}