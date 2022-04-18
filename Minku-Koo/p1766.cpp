
#include <iostream>
#include <stdio.h>
#include <queue>
#include <vector>
#define NM 32001
#define MM 100001

using namespace std;
// 2차원 vector
vector<vector<int>> v(NM, vector<int>()) ;
// 출력을 담을 queue
queue<int> q;
// 들어갈 우선순위 queue
priority_queue<int, vector<int>, greater<int>> start ;
// 입력 차수를 계산할 배열
int arr[NM];


int solution(int all){
	
	// start node 계산
	for(int i=1; i<=all; i++)
		if(arr[i]==0)
			start.push(i);
	
	while(!start.empty()){
		int node = start.top();
		// 시작 차수를 빼내고, queue에 추가
		start.pop(); q.push(node);
		// 만약 더이상 찾아갈 노드가 없으면 종료
		if(v[node].size()==0) continue;
		// 모든 노드 계산
		for(int j=0; j<v[node].size(); j++){
			int e = v[node][j];
			
			// 노드에서 차수 제거
			arr[e]--;
			// 만약 들어오는 차수가 없을 경우, 시작 노드에 추가
			if(arr[e]==0) start.push(e);
		}
	}
	
	return 0;
}

int main(void){
	
	int N, M, a, b;
	
	scanf("%d %d", &N, &M);
	
	for(int k=0; k<M; k++){
		cin >> a >> b ;
		// vector 삽입
		v[a].push_back(b);
		// 들어오는 차수 증가
		arr[b]++;
	}
	
	solution(N);
	// 모든 queue 순차 출력
	while(!q.empty()){
		printf("%d ", q.front());
		q.pop();
	}
	
	return 0;
}

