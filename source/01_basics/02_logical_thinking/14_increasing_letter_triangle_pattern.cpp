#include<iostream>
using namespace std;

void increasingLetterTraingle(int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<=i;j++){
            cout<<char('A'+j)<<" ";
        }
        cout<<endl;
    }
}
int main() {
    increasingLetterTraingle(5);
    return 0;
}