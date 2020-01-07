#include<iostream>
#include<vector>

using namespace std;

int subArraySum(vector<int> array,int n, int s){
    int current_sum = array[0];
    int start = 0;

    int i = 1;

    while(i <= n){
        while(current_sum > s && start < i -1){
            current_sum -= array[start];
            start++;
        }

        if(current_sum == s){
            printf("%d %d\n", start+1, i);
            return 1;
        }

        if(i < n){
            current_sum += array[i];
        }
    }

    return 0;
}

int main(){
    int T;

    cin >> T;

    for(int i = 0; i < T; i++){
        int N, S;
        cin >> N >> S;

        vector<int> array(N);
        printf("%d %d", N, S);
        for(int j = 0; j < N; j++){
            cin >> array[j];
            print("%d kkk", array[j]);
        }
        printf("%d", array[0]);
        if(subArraySum(array, N, S) == 0) printf("-1\n");

    }

    return 0;
}