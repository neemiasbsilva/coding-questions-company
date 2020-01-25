#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

class Graph{
    public:
    vii *adj;
    int V;

    Graph(int V);
    void addEdgestwo(int u, int v, int p);
    void addEdgesone(int u, int v, int p);
    int dijkstra(int s, int C);
};

Graph::Graph(int V){
    this->V = V;
    adj = new vii[V];
}

void Graph::addEdgestwo(int u, int v, int p){
    adj[u].push_back(ii(v, p));
    adj[v].push_back(ii(u, p));
}

void Graph::addEdgesone(int u, int v, int p){
    adj[u].push_back(ii(v, p));
}

int Graph::dijkstra(int s, int C){
    vi dist(V, INT_MAX), visited(V, 0);
    dist[s] = 0;

    priority_queue<ii, vii, greater<ii> > pq; pq.push(ii(0, s));

    while(!pq.empty()){
        ii front = pq.top(); pq.pop();
        int d = front.first, u = front.second;
        //if(d > dist[u]) continue;
        if(!visited[u]){
            visited[u] = 1;
            for(int i = 0; i < (int) adj[u].size(); i++){
                ii v = adj[u][i];
                if(dist[u]+v.second < dist[v.first]){
                    dist[v.first] = dist[u] + v.second;
                    pq.push(ii(dist[v.first], v.first));
                }
            }
        }
    }

    return dist[C];
}

int main(){
    int N, M, C, K;
    while(cin >> N >> M >> C >> K, !(N==0 && M == 0 && C == 0 && K == 0)){
        Graph g(N);
        for(int i = 0; i < M; i++){
            int u, v, p; cin >> u >> v >> p;
            //if the roads has out of roates
            if(u >= C && v >= C){
                g.addEdgestwo(u, v, p);
            }
            
            if(u < C && v < C){
                g.addEdgesone(u, v, p);
            }

            //if the roads are interconections
            if(u < C && v < C && abs(u-v) == 1){
                g.addEdgestwo(u, v, p);
            }

        }
        C--;
        cout << g.dijkstra(K, C) << endl;
        
    }
    return 0;
}
