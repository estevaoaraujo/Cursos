import java.util.Scanner;

public class Exercicio3 {
    //Faça um Programa que peça dois números e imprima a soma.

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite dois valores: ");
        float n1 = scanner.nextFloat();
        float n2 = scanner.nextFloat();

        float resutaldo = n1 + n2 ;

        System.out.println(resutaldo);

        scanner.close();
    }
}
