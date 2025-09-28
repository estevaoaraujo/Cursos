import java.util.Scanner;

public class Exercicios1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Declarando o vetor de 5 números inteiros
        int[] vetor = new int[5];

        // Lendo os números e armazenando no vetor
        System.out.println("Digite 5 números inteiros:");

        for (int i = 0; i < vetor.length; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            vetor[i] = scanner.nextInt();
        }

        // Exibindo os números do vetor
        System.out.println("\nNúmeros digitados:");

        for (int i = 0; i < vetor.length; i++) {
            System.out.println("Número " + (i + 1) + ": " + vetor[i]);
        }

        scanner.close();
    }
}

