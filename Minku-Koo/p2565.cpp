//
#include <iostream>
#include <stdio.h>
#define NUMMAX 501

using namespace std;

int temp[NUMMAX]; // 입력 받기 위한 배열
int arr[NUMMAX]; // 입력을정렬하기 위한 배열
int sortLen[NUMMAX]; // 최대 오름차순을 계산하기 위한 배열
int arrLen; // 전깃줄 최대 값을 저장하기 위한 전역 변수

int solution(int line){
	if(line==1) return 0;
	
	int ans = 0; 
	// 모든 전깃줄 계산
	for(int k=2; k<=line; k++){
		int now = arr[k]; // 현재 전깃줄 위치
		
		if(now==0) continue; // 0이면 제외
		
		int maxLen = 0; // 이전 값중 최대 오름차순 값
		for(int j=1; j<k; j++){ // 첨부터 이전까지의 값 검사
			// now보다 작은 수 중에서
			// sortLen이 가장 긴 것 + 1
			if(now > arr[j]) // now보다 작은 값 중
				// 최대 오름차순 값 갱신
				if(maxLen < sortLen[j] ) 
					maxLen = sortLen[j];
		}
		
		// 최대 오름차순 + 1 값 = 현재 최대 오름차순 값
		sortLen[k] = maxLen + 1;
		if(ans < sortLen[k])
			ans = sortLen[k];
	}
	// 정답 계산
	return line - ans;
}


int main(void){
	
	int line, a, b;
	
	scanf("%d", &line);
	
	temp[NUMMAX] = {0,};
	arr[NUMMAX] = {0,};
	sortLen[NUMMAX] = {0,};
	sortLen[1] = 1;
	arrLen = 0;
	
	for(int k=0; k<line; k++){
		cin >> a >> b ;
		temp[a] = b ;
		if(arrLen < a) arrLen = a;
	}
	
	int cnt = 1;
	// 입력 값을 정렬해줌
	for(int k=1; k<=arrLen; k++)
		if(temp[k]!=0)
			arr[cnt++] = temp[k];
	
	printf("%d", solution(line));
	
	return 0;
}

