#include<iostream>
using namespace std;

void diamondStarPyramid(int n){

    for(int i=n;i>0;i--){
        //space
        for(int j=1;j<i;j++){
            cout<<"  ";
        }
        //stars
        for(int j=0;j<=2*(n-i);j++){
            cout<<"* ";
        }
        cout<<endl; 
    }
    for(int i=n-1;i>0;i--){
        //space
        for(int j=0;j<n-i;j++){
            cout<<"  ";
        }
        //stars
        for(int j=2*(i)-1;j>0;j--){
            cout<<"* ";
        }
        cout<<endl; 
    }
}
int main() {
    diamondStarPyramid(5);
    return 0;
}