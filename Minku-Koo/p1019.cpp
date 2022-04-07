//
#include <stdio.h>

long long arr[10] = {0};
long long div = 1;


int main(){
	long long page;
	scanf("%lld", &page);
	
	while(page>=div){
		
		int moc = page / (div*10);
		int now = (page%(div*10)) / div;
		
		if(moc>0) {
			for(int a=0; a<10 ; a++)
				arr[a] += (moc)  * div;
			if(now==0)
				arr[0] -=  div;
		}
		
		for(int k=1; k< now  ;k++)
			arr[ k] +=  div ;
		arr[now] += page % (div) +1;
		
		div *= 10;
	}
	
	for(int i=0; i<10; i++) printf("%d ", arr[i]);
	
	return 0;
}