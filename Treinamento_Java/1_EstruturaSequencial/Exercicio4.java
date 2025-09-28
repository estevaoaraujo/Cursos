//Faça um Programa que peça as 4 notas bimestrais e mostre a média.

import java.util.Scanner;

public class Exercicio4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Insira o valor e aperte enter: ");
        float n1 = scanner.nextFloat();
        float n2 = scanner.nextFloat();
        float n3 = scanner.nextFloat();
        float n4 = scanner.nextFloat();
        float resultado = (n1+n2+n3+n4)/4; 

        System.out.println("A media das notas são: "+ resultado);

        scanner.close();
    }
}
