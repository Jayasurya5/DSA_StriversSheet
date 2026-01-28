#include<iostream>
using namespace std;

void alphaRamp(int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<=i;j++){
            cout<<char('A'+i)<<" ";
        }
        cout<<endl;
    }

}
int main() {
    alphaRamp(5);
    return 0;
}