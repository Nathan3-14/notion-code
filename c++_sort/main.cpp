#include <iostream>
#include <list>
using namespace std;

list<int> sort(list<int> _list) {
    list<int> sorted_list = {};
    return _list;
}

int main() {
    string ln = "\n";

    cout << "hi!" << ln;
    list<int> __list = sort({1, 2, 3});
    for (int item: __list) {
        cout << item << ",";
    }
}
