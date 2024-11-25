#include <iostream>
#include <cmath>
#include <cstdlib>
#include <iomanip>

using std::cout;
using std::cin;
using std::endl;
using std::string;

int main(int argc, const char** argv) {
    int sum = 0;

    for (int i = 0; i < 20; i++){
        sum += i;
        cout << "i = " << i << "\tsum = " << sum << endl;
        
    }

    return 0;
}