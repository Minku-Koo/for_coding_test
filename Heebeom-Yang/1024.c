#include <stdio.h>

int N, L, div, remain;
int sum = 0;

int get_sum(int* arr) {
    int result = 0;

    for(int i = 0; i < L; i ++) {
        if(arr[i] >= 0)
            result += arr[i];
    }
    
    return result;
}

int main() {
    scanf("%d %d", &N, &L);
        
    int answer[100] = {0, };

    while(L <= 100) {
        remain = N % L;
        div = N / L;
        sum = 0;
        if(L % 2 == 0) {
            if(remain == L / 2) {
                int end = div + (L / 2);
                int start = end - L + 1;
                for(int i = 0; i < L; i ++)
                    answer[i] = start + i;

                sum = get_sum(answer);
                if(sum == N)
                    break;
            }
            
        } else {
            if(remain == 0) {
                int start = div - (L / 2);
                for(int i = 0; i < L; i ++)
                    answer[i] = start + i;
                
                sum = get_sum(answer);
                if(sum == N)
                    break;
            }
        }
        
        L ++;
    }
    
    if(L <= 100) 
        for(int i = 0; i < L; i ++) {
            printf("%d ", answer[i]);
        }
    else
        printf("-1");
    return 0;
}