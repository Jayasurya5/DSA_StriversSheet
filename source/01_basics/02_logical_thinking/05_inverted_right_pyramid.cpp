#include<iostream>
using namespace std;

void invertedRightPyramid(int n){
    for(int i=n;i>=0;i--){
        for(int j=1;j<=i;j++){
            cout<<"* ";
        }
        cout<<endl;
    }
}
int main() {
    invertedRightPyramid(5);
    return 0;
}