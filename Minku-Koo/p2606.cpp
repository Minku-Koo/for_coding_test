#include <stdio.h>
#include <iostream>
#include <queue> 
#define MAX 101
std::queue<int> q; 

int arr[MAX][MAX] = {0,};
int check[MAX] = {0,};
int cnt[MAX]={0,};

using namespace std; 

int solution(void){
	// q 1번 컴퓨터 넣기
	int node, result=0;
	for(int j=0; ;j++){
		node = arr[1][j];
		if(node==0) break;
		q.push(node);
		result++;
		check[node] =1;
	}
	
	// 반복문 큐 사라질때까지
	while(!q.empty()){
		node = q.front();
		q.pop();
		
		for(int j=0; ;j++){
			if(arr[node][j]==0) break;
			if(check[arr[node][j]]>0) continue;
			q.push(arr[node][j]);
			check[arr[node][j]] =1;
			result++;
		}
	}
	return result - 1;
}

int main(void){
	int ind, computer, net, side;
	scanf("%d %d", &computer, &net);
	for(int k=0; k<net; k++){
		scanf("%d", &ind);
		scanf("%d",  &arr[ind][cnt[ind]++]);
		
		// 양방향 그래프이니 이 부분 추가해줘야함. 매우 중요!!
		side = arr[ind][cnt[ind]-1];
		arr[side][cnt[side]++] = ind;
	}
	
	printf("%d", solution());
	return 0;
}
