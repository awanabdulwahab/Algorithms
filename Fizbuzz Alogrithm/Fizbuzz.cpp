#include<iostream>

using namespace std;

int main(){
int numberList[15] = { 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 };
int sizeofArray = sizeof(numberList) / sizeof(numberList[0]);
    int i = 0;
    for(i = 0; i< sizeofArray; i++){
        if (numberList[i] % 15 == 0){
            cout<<"Fizbuzz"<<endl;
        }
        else if (numberList[i] %3 == 0){
            cout<<"Fizz"<<endl;
        }
        else if (numberList[i] %5 ==0) {
            cout<<"Buzz"<<endl;
        }
        else{
            cout<<numberList[i]<<endl;
        }
    }
    return 0;
}