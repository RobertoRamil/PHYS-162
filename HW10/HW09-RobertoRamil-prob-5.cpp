#include <iostream>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <String>
#include <fstream>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::ofstream;

const double PI = std::acos(-1);


double p(double x);

int main(int argc, const char** argv) {

    ofstream MyFile("P5-data.txt");
    double jump = (2.*PI)/11.;
    cout << std::setprecision(8);

    for (double x = 0; x < 2.*PI; x+=jump){
        cout << "x = " << x << "\ty = " << p(x) << endl;
    }
    cout << "\n\n\n";
    cout << "Now doing it for 101 values\n";
    jump = (2.*PI)/101.;
    for (double x = 0; x < 2.*PI; x+=jump){
        cout << "x = " << x << "\ty = " << p(x) << endl;
        MyFile << "x = " << x << "\ty = " << p(x) << endl;
    }

    MyFile.close();
    return 0;
}

double p(double x){
    return pow(x,2);
}
