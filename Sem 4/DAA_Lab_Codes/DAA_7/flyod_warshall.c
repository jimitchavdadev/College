#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
struct Edge {
int src, dest, weight;
};
int** allocateMatrix(int V) {
int **matrix = (int **)malloc(V * sizeof(int *));
for (int i = 0; i < V; i++) {
matrix[i] = (int *)malloc(V * sizeof(int));
for (int j = 0; j < V; j++)
matrix[i][j] = (i == j) ? 0 : INT_MAX; 
}
return matrix;
}
void printMatrix(int **matrix, int V, const char *name) {
printf("%s:\n", name);
for (int i = 0; i < V; i++) {
for (int j = 0; j < V; j++) {
if (matrix[i][j] == INT_MAX)
printf("INF\t");
else
printf("%d\t", matrix[i][j]);
}
printf("\n");
}
printf("\n");
}
void floydWarshall(int **graph, int V) {
int **dist = allocateMatrix(V); // Output matrix that will have the shortest distances between every pair of vertices
for (int i = 0; i < V; i++)
for (int j = 0; j < V; j++)
dist[i][j] = graph[i][j];
for (int k = 0; k < V; k++) {
printMatrix(dist, V, "Intermediate Matrix");
for (int i = 0; i < V; i++) {
for(int j = 0; j < V; j++) {
if (dist[i][k] != INT_MAX && dist[k][j] != INT_MAX && dist[i][k] + dist[k][j] < dist[i][j])
dist[i][j] = dist[i][k] + dist[k][j];
}
}
}
printMatrix(dist, V, "Final Shortest Distance Matrix");
for (int i = 0; i < V; i++)
free(dist[i]);
free(dist);
}
void addEdges(int **graph, struct Edge edges[], int E) {
for (int i = 0; i < E; i++) {
graph[edges[i].src][edges[i].dest] = edges[i].weight;
}
}
int main() {
int V = 4;
int E = 6; 
int **graph = allocateMatrix(V);
struct Edge edges[] = {
{0,1,-1},
{0,2,4},
{1,2,3},
{1,3,2},
{1,4,2},
{3,2,5},
{3,1,1},
{4,3,-3}
};
addEdges(graph, edges, E);
printf("Initial adjacency matrix:\n");
printMatrix(graph, V, "Initial Adjacency Matrix");
floydWarshall(graph, V);
for (int i = 0; i < V; i++)
free(graph[i]);
free(graph);
return 0;
}