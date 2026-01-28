#include<iostream>
using namespace std;

void alphaTriangle(int n){
    for(int i=0;i<n;i++){
        for(int j=n-i;j<=n;j++){
            cout<<char('A'+j-1)<<" ";
        }
        cout<<endl;
    }

}
int main() {
    alphaTriangle(5);
    return 0;
}