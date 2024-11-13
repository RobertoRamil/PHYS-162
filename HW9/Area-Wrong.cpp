#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

constexpr double PI = std::acos(-1);

int main(int argc, char** argv){
    double radius, circum, area;

    cout << "pi = " << setprecision(16) << PI << endl;
    cout << "Enter a radius in Meters: ";
    cin >> radius;

    circum = 2.*PI*radius;
    area = PI *pow(radius,2);
    cout << "Radius: " << radius << " m" << endl;
    cout << "Circumference: " << circum << " m"<<endl;
    cout << "Area: " << area << " m²" << endl;

    system("pause");
    return EXIT_SUCCESS;
}