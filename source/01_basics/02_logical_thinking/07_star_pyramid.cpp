#include<iostream>
using namespace std;

void starPyramid(int n){

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

    //2 * i-1 times we should print

}
int main() {
    starPyramid(5);
    return 0;
}