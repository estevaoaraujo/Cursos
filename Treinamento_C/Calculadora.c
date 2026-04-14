#include <stdio.h>

int main() {
    char operacao;
    double n1, n2;

    printf("--- Calculadora do Estevao ---\n");
    printf("Escolha a operacao (+, -, *, /): ");
    scanf(" %c", &operacao); // O espaco antes do %c ignora o 'enter' anterior

    printf("Digite o primeiro numero: ");
    scanf("%lf", &n1);
    printf("Digite o segundo numero: ");
    scanf("%lf", &n2);

    printf("\nResultado: ");
    switch (operacao) {
        case '+':
            printf("%.2lf + %.2lf = %.2lf", n1, n2, n1 + n2);
            break;
        case '-':
            printf("%.2lf - %.2lf = %.2lf", n1, n2, n1 - n2);
            break;
        case '*':
            printf("%.2lf * %.2lf = %.2lf", n1, n2, n1 * n2);
            break;
        case '/':
            if (n2 != 0)
                printf("%.2lf / %.2lf = %.2lf", n1, n2, n1 / n2);
            else
                printf("Erro! Divisao por zero nao existe.");
            break;
        default:
            printf("Operacao invalida!");
    }
    printf("\n----------------------------\n");

    return 0;
}