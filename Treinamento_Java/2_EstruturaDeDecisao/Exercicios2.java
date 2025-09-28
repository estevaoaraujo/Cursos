//Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo
import java.util.Scanner;

public class Exercicios2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("-> ");
        int valor = scanner.nextInt();

        if(valor>=0){
            System.out.println("Valor é positivo " + valor);
        }else{
            System.out.println("Valor negativo " + valor);
        }

        scanner.close();
    }
}
