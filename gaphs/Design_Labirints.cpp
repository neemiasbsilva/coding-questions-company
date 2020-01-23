#include <iostream>
#include <list>

#define endl "\n"
using namespace std;
int cont = 0;
class Graph{
    int V;
    list<int> *adj;
    void DFSUtil(int v,bool visited[]);
    public:
    Graph(int V);
    void addEdge(int v, int w);
    void DFS(int v);
};

Graph::Graph(int V){
    this->V = V;
    adj = new list<int>[V];
}

void Graph::addEdge(int v, int w){
    adj[v].push_back(w);
    adj[w].push_back(v);
}

void Graph::DFSUtil(int v, bool visited[]){
    visited[v] = true;

    list<int>::iterator i;
    for(i = adj[v].begin(); i != adj[v].end(); i++){
        if(!visited[*i]){
            cont++;
            DFSUtil(*i, visited);
            cont++;
        }
    }
    
}

void Graph::DFS(int v){
    bool *visited = new bool[V];

    for(int i = 0; i < V; i++) visited[i] = false;
    DFSUtil(v, visited);
}

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int T; cin >> T;

    while(T--){
        cont=0;
        int n; cin >> n;
        int V, E; cin >> V >> E;
        Graph g(V);
        for(int i = 0; i < E; i++){
            int v, w; cin >> v >> w;
            g.addEdge(v, w);
        }
        g.DFS(n);
        cout << cont << endl;
    }
    return 0;
}