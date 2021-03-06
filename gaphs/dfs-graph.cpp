#include <iostream>
#include <vector>
#include <stack>
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
        void dfs(int u, bool visited[]);
};
stack<int> s;
Graph::Graph(int V){
    this->V = V;
    AdjList = new vi[V];
}

void Graph::dfs(int u, bool visited[]){
    visited[u] = true;
    s.push(u);
    cout << u << ' ';
    for(int j = 0; j < (int) AdjList[u].size(); j++){
        int v = AdjList[u][j];
        

        if(!visited[j])
            dfs(v, visited);
    }
}

void Graph::addEdge(int u, int v){
    AdjList[u].push_back(v);
    // AdjList[v].push_back(u);
}




int main(){
    int n_test;
    cin >> n_test;

    while(n_test--){

        int V, E;
        cin >> V >> E;
        Graph g(V);
        for(int i = 0; i < E; i++){
            int u, v;
            cin >> u >> v;
            g.addEdge(u, v);
        }
        bool *visited = new bool[V];

        for(int i = 0; i < V; i++) visited[i] = false;
        g.dfs(0, visited);
        cout << endl;
        while(!s.empty()){
            cout << s.top(); s.pop();
        }
        cout << endl;
    }
    return 0;
}