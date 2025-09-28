import java.util.Scanner;

public class Exercicio5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Digite a medida em metros: ");
        float metros = scanner.nextFloat();
        
        float centimetros = metrosParaCentimetros(metros);
        
        System.out.println(metros + " metros equivalem a " + centimetros + " centímetros.");
        
        scanner.close();
    }
    
    public static float metrosParaCentimetros(float metros) {
        float centimetros = metros * 100;
        return centimetros;
    }
}
