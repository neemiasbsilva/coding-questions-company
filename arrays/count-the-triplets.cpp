/*
For check the question, please copy this link in your
browser: https://practice.geeksforgeeks.org/problems/count-the-triplets/0
Thanks :)
*/

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

void count_triplest(vector<int> array, int N){
    int max_val = 0;

    for(int i = 0; i < N; i++)
        max_val = max(max_val, array[i]);
    
    int frequence[max_val + 1];
    for(int i = 0; i < max_val+1; i++){
        frequence[i] = 0;
    }

    for(int i = 0; i < N; i++){
        frequence[array[i]]++;
    }

    int ans = 0;
    //Case 1: (0, 0, 0)
    ans += frequence[0] * frequence[0]-1 * frequence[0]-2 / 6;

    //Case 2: (0, x, x)
    for(int i = 1; i <= max_val; i++){
        ans += frequence[0] * frequence[i] * (frequence[i] -1) / 2;
    }

    //Case 3: ()
    for()

}

int main(){
    int T; //number of test case
    cin >> T;
    while(T--){
        int N, sum = 0, cont = 0, triplets = 0;
        cin >> N;
        vector<int> array (N);
        for (int i = 0; i < N; i++)
        {
            cin >> array[i];
        }
        
        count_triplest(array, N)
    }

    return 0;
}