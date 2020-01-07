/*
For check the question, please copy this link in your
browser: https://practice.geeksforgeeks.org/problems/count-the-triplets/0
Thanks :)
*/

#include<iostream>
#include<vector>

using namespace std;

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
        
        for(int i = 0; i < N; i++){
            sum += array[i];
            cont = 1;
            for(int j = i+1; j < N; j++){
                if(array[j] > array[j-1])
                    sum+= array[i];
                    cont++;
                
                if(cont == 3){
                    if(sum == array[j])
                        triplets++;
                    sum = array[i];
                }
            }
        }
        if(triplets > 0) cout << triplets << endl;
        else cout << "-1" << endl;
    }

    return 0;
}