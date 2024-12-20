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
using std::ifstream;
using std::vector;
using std::min;


double scalarProduct (vector<double> a, vector<double> b);

double magnitude(vector<double> vec);

vector<double> normalize(const vector<int> &vec);

vector<double> transformToNewBias(vector<vector<double>> &bias,vector<double> &vec);

int main(int argc, const char** argv) {
    ifstream myFile("basis.txt");
    vector<double> a;
    vector<double> b;
    vector<double> c;
    int data;

    if(myFile.is_open()){
        cout << "File Opened Successfully" << endl;
    } else {
        std::cerr << "Error opening file" << endl;
        return EXIT_FAILURE;
    }
    for(int y = 0; y < 3; y++){
        if(y == 0){
            for(int i = 0; i < 3; i++){
                myFile >> data;
                a.push_back(data);
            }
        }
        if(y == 1){
            for(int i = 0; i < 3; i++){
                myFile >> data;
                b.push_back(data);
            }
        }
        if(y == 2){
            for(int i = 0; i < 3; i++){
                myFile >> data;
                c.push_back(data);
            }
        }
    }
    myFile.close();

    vector<double> normalizeA = normalize(a);

    return EXIT_SUCCESS;
}

double scalarProduct(vector<double> vec1, vector<double> vec2){
    double prod = 0;
    for (int i = 0; i < std::min(vec1.size(),vec2.size()); i++){
        prod += (vec1.at(i) * vec2.at(i));
    }

    return prod;
}

double magnitude(vector<double> vec){
    double sum = 0;
    for (int i = 0; i < vec.size(); i++){
        sum += vec.at(i) * vec.at(i);
    }
    
    return sqrt(sum);
}

vector<double> normalize(vector<int> &vec){
    
    return vector<double>();
}

vector<double> transformToNewBias(vector<vector<double>> &bias, vector<double> &vec){
    
    return vector<double>();
}
