#include <iostream>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <String>

using std::cout;
using std::cin;
using std::endl;
using std::string;

int main(int argc, const char** argv) {

   string name;
   int year, answ;

    cout << "Please enter your full name: "<< endl;
    getline(cin, name);

    cout << "Please enter the year: " << endl;
    cin >> year;

    cout << "What is the answer to 2+2" << endl;
    cin >> answ;

    cout << "Hello, " << name << "!\nThe year is " << year << endl;

    if (answ == 4){
        cout << "The answer you entered is correct, 2 + 2 = " << answ << endl;
    }
    else cout << "The answer you entered is incorrect , 2 + 2 \u2260 " << answ << endl;


    return 0;
}