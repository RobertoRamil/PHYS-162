#include <iostream>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <String>

using std::cout;
using std::cin;
using std::endl;
using std::string;


int main(){

    int age, weight, height;

    cout << "Enter your age in years\n";
    cin >> age;
    cout << "Enter your weight in Kilograms\n";
    cin >> weight;
    cout << "Enter your height in centimeters\n";
    cin >> height;

    if(age >=16){
        cout << "You are old enough to drive\n\n";
    } else cout << "You are not old enought to drive\n\n";

    if(age >19 || age < 30){
        cout << "You are in your twenties\n\n";
    } else cout << "You are not in your twenties\n\n";

    if(age < 22 && weight < 65){
        cout << "You are less than 22 and weight less than 65\n\n";
    } else if (age > 26 && height > 180){
        cout << "You are older than 26 and taller than 180cm\n\n";
    }
    


    return EXIT_SUCCESS;
}