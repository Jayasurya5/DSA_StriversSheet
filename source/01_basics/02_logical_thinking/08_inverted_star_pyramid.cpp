#include<iostream>
using namespace std;

void invertedStarPyramid(int n){
    for(int i=n;i>0;i--){
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

    //2 * i-1 times we should print

}
int main() {
    invertedStarPyramid(5);
    return 0;
}