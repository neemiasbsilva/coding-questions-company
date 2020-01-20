#include <iostream>

using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

vi dfs_num;


void addEdge(vii AdjList, int u, int v){
    AdjList[u].push_back(v);
    AdjList[v].push_back(u);
}


int main(){

    return 0;
}