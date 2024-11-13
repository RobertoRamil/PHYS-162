#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <cmath>

using std::cout;
using std::cin;
using std::endl;

constexpr double PI = std::acos(-1);

double vol(double radius){
    return (4/3)*PI*pow(radius,2);
}
double surfaceArea(double radius){
    return 4*PI*pow(radius,2);
}

int main(int argc, char** argv){
    double radius, volume, SA;

    cout << "pi = " << std::setprecision(16) << PI << endl;
    cout << "Enter a radius in Meters: ";
    cin >> radius;

    volume = vol(radius);
    SA = surfaceArea(radius);
    cout << "Radius: " << radius << " m" << endl;
    cout << "Volume: " << volume << " m"<< endl;
    cout << "Surface Area: " << SA << " m^2" << endl;

    system("pause");
    return EXIT_SUCCESS;
}