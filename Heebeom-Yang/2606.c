#include <stdio.h>
 
int arr[101][101] = { 0, };
int visit[101] = { 0, }; 
int result = 0;


void DFS(int start, int vertex_num) {
    visit[start] = 1;

    result ++;

    for(int i = 1; i <= vertex_num; i ++){
        if(arr[start][i] == 1 && visit[i] == 0)
            DFS(i, vertex_num);
    }
}
 

int main(){
    int vertex_num, link_num, x, y;

    scanf("%d", &vertex_num);
    scanf("%d", &link_num);

    for(int i = 0; i<link_num; i++){
        scanf("%d %d", &x, &y);
        arr[x][y]  =  1;
        arr[y][x]  =  1;
    }
    
    DFS(1, vertex_num);
    printf("%d", -- result);

    return 0;
}