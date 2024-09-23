#include <iostream>
#include<list>

std::list<int> cool_thingy(int number1, int number2) {
    return {number1, number2};
}
int main() {

    std::cout << "Hello World!\n";
    std::cout << cool_thingy(1, 2) << "\n";
    return 0;
}