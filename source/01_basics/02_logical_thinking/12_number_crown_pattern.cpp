#include<iostream>
using namespace std;

void numberCrownPattern(int n){
    for(int i=0;i<n;i++){
        for(int j=1;j<=i+1;j++){
            cout<<j<<" ";
        }
        for(int j=0;j<2*(n-i-1);j++){
            cout<<"* ";
        }
        //IMP
        for(int j=i+1;j>0;j--){
            cout<<j<<" ";
        }
        cout<<endl;
    }
}
int main() {
    numberCrownPattern(5);
    return 0;
}