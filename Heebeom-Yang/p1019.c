#include <stdio.h>

int answer[10] = {0, };
int digit_num = 1;

void calc(int num) {
    while(num != 0) {
        answer[num % 10] += digit_num;
        num /= 10;
    }
}

int main() {
    int start_page = 1;
    int end_page;
    
    scanf("%d", &end_page);

    while(start_page <= end_page) {
        while((end_page % 10 != 9) && (start_page <= end_page)) {
            calc(end_page);
            end_page --;
        }
        
        if(start_page > end_page)
            break;

        while((start_page % 10 != 0) && (start_page <= end_page)) {
            calc(start_page);
            start_page ++;
        }
        
        start_page /= 10;
        end_page /= 10;

        for(int i = 0; i < 10; i ++)
            answer[i] += (end_page - start_page + 1) * digit_num;

        digit_num *= 10;
    }

    for(int i = 0; i < 10; i ++)
        printf("%d ", answer[i]);

    return 0;
}
