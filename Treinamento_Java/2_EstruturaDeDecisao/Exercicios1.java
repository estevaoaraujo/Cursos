//Faça um Programa que peça dois números e imprima o maior deles.
import java.util.Scanner;

public class Exercicios1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite dois número inteiro: ");
        
        int v1 = scanner.nextInt();
        int v2 = scanner.nextInt();

        if(v1>v2){
            System.out.println(" O manior valor é "+ v1);
        }else{
            System.out.println("Maior valor é "+ v2);
        }

        scanner.close();
    }
    
}