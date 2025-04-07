#include <stdio.h>
#include <limits.h>
#include <string.h>
#include <stdlib.h>

#define max 100  // maximum no: of nodes

int bfs(int resgraph[max][max], int src, int sink, int parent[], int nodes) {
    int visit[max] = {0}; 
    int queue[max], front = 0, rear = 0;

    queue[rear++] = src;
    visit[src] = 1;
    parent[src] = -1;  

    while (front < rear) {
        int u = queue[front++];
        
        for (int v = 0; v < nodes; v++) {
            if (!visit[v] && resgraph[u][v] > 0) {
                queue[rear++] = v;
                parent[v] = u;  
                visit[v] = 1;

                if (v == sink) return 1;  
            }
        }
    }
    return 0;  
}

// Algo for max flow in network using Edmonds-Karp algorithm 
int edmondsKarp(int graph[max][max], int src, int sink, int nodes){
    int resgraph[max][max];
    memcpy(resgraph, graph, sizeof(resgraph));  

    int parent[max];  
    int maxFlow = 0;

    while (bfs(resgraph, src, sink, parent, nodes)) {
        int flow = INT_MAX; //path flow
        
        for (int v = sink; v != src; v = parent[v]) {
            int u = parent[v];
            flow = (flow < resgraph[u][v]) ? flow : resgraph[u][v];
        }

        for (int v = sink; v != src; v = parent[v]) {
            int u = parent[v];
            resgraph[u][v] -= flow;
            resgraph[v][u] += flow;  
        }

        maxFlow += flow;  // augment flow
    }
    return maxFlow;
}

int main() {
    int nodes, edges, u, v, capa;
    int graph[max][max] = {0};

    printf("Enter the number of nodes and edges: ");
    if (scanf("%d %d",&nodes,&edges) != 2|| nodes <= 0||edges < 0) {
        printf("Invalid input! Please enter valid values for nodes and edges.\n");
        return 1;
    }

    printf("Enter the edges with capacities (u v capacity):\n");
    for (int i = 0; i < edges; i++) {
        scanf("%d %d %d", &u, &v, &capa);
        graph[u][v] = capa; 
    }

    int src, sink;
    printf("Enter source and sink: ");
    scanf("%d %d", &src, &sink);
    

    int maxFlow = edmondsKarp(graph, src, sink, nodes);
    printf("The maximum possible flow is: %d\n", maxFlow);

    return 0;
}