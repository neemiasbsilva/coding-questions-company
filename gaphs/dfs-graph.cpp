#include <iostream>
#include <vector>

#define D(x) cout << #x << " = " << (x) << endl
#define endl '\n'

using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

vi dfs_num;

class Graph{
    public:
        int V;
        vi *AdjList;
        Graph(int V);
        void addEdge(int u, int v);
        void dfs(int u);
};

Graph::Graph(int V){
    this->V = V;
    AdjList = new vi[V];
}


void Graph::addEdge(int u, int v){
    AdjList[u].push_back(v);
    AdjList[v].push_back(u);
}


void Graph::dfs(int u){
    dfs_num
}

int main(){
    int n_test;
    cin >> n_test;

    while(n_test--){

        int V, E;
        cin >> V >> E;
        Graph g(V);
        for(int i = 0; i < V; i++){
            int u, v;
            cin >> u >> v;
            g.addEdge(u, v);
        }
    }
    return 0;
}