#include <stdio.h>
int main(){
	
	int n, ln, first;
	scanf("%d %d", &n, &ln);
	
	// ln이 짝수 > 양 사이드 합이 n/(ln/2) 되어야함
	// ln이 홀수 > 중앙값이 n/ln
	while(1){
		if(ln%2==0){ //짝
			if(n%(ln/2)==0){ // 짝에서 해를 구할 수 있을 때
				int sum = n/(ln/2);
				// x + (x + (ln-1)) = sum
				// 2*x + ln - 1 = sum
				// x = (sum + 1 - ln) / 2
				if((sum + 1 - ln)%2==0) {
					first = (sum + 1 - ln) / 2;
					if(first>=0) break;
				}
			}
			
		}else{ // 홀
			if((n%ln)==0){ // 홀에서 해를 구할 수 있을 때
				int center = n/ln; // 중앙값 계산
				first = center - (ln/2);
				if(first>=0)break;
			}
		}
		
		if(ln>100||ln>n*2) break; // 예외 처리
		ln++;
	}
	
	if(ln>100||ln>n*2) printf("%d ", -1);
	else
		for(int j=0; j<ln; j++)
			printf("%d ", first+j);
		
	return 0;
}