#include<iostream>
using namespace std;

void invertedNumberedRightPyramid(int n){
    for(int i=n;i>=0;i--){
        for(int j=1;j<=i;j++){
            cout<<j<<" ";
        }
        cout<<endl;
    }
}
int main() {
    invertedNumberedRightPyramid(5);
    return 0;
}