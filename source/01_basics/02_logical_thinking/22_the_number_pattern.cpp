#include<iostream>
using namespace std;
//IMP
void numberPattern(int n){
    int size = 2 * n - 1;
    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            int top=i;
            int left=j;
            int right =size-j-1;
            int bottom = size-i-1;
            int value = n - min(min(top,bottom),min(left,right));
            cout<<value<<" ";
        }
        cout<<endl;
    }
}
int main() {
    numberPattern(5);
    return 0;
}