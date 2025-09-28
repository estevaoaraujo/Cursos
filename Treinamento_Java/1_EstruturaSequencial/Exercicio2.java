import java.util.Scanner;

// Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

public class Exercicio2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Digite um valor: ");
        int numero = scanner.nextInt();

        System.out.println(numero);

        scanner.close();
    }
}
