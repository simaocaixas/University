/* iaed24 - ist1109632 - lab03/ex01 */
#include <stdio.h>

int main() {
    int N, Cruz_L, Cruz_R, Linhas = 1, Posicao;
    scanf("%d", &N);

    Cruz_L = 1;
    Cruz_R = N;

    while (Linhas <= N) {
        Posicao = 1; 
        
        while (Posicao <= N) {
            if (Posicao == Cruz_L || Posicao == Cruz_R) {
                printf("*");
            }
            else {
                printf("-");
            }

            if (Posicao != N) { 
                printf(" ");
            }

            Posicao += 1;
        }

        Cruz_L += 1;
        Cruz_R -= 1;
        Linhas += 1;
        printf("\n");
    }
    return 0;
}

