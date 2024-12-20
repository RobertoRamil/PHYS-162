#include <iostream>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <fstream>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::ofstream;
using std::vector;

double scalarProduct (vector<double> a, vector<double> b);


int main(int argc, const char** argv) {

    vector<double> a;
    vector<double> b;

    a = {1, 5, 4};
    b = {7, -2, 9};

    if(a.size() != b.size()){
        cout << "Warning Vectors are not the same size" << endl;
    }    
    cout << "Scalar Product of a and b = " << scalarProduct(a, b) << endl;
    cout << endl;

    a = {4, 1, 6};
    b = {10, -3};

    if(a.size() != b.size()){
        cout << "Warning Vectors are not the same size" << endl;
    }    
    cout << "Scalar Product of a and b = " << scalarProduct(a, b) << endl; 
    


    return EXIT_SUCCESS;
}

double scalarProduct(vector<double> a, vector<double> b){
    double prod = 0;
    for (int i = 0; i < std::min(a.size(),b.size()); i++){
        prod += (a.at(i) * b.at(i));

    }

    return prod;
}
