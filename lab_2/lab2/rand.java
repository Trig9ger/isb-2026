import java.io.*;

public class rand{
    public static void main(String args[]){
        char[] Result = new char[128];

        for (int i = 0; i < 128; i++) {
            Result[i] = (char) (Math.random()*2 + '0');
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter("javarand.txt"))) {
            writer.write(Result);
        } catch (IOException e) {
            System.err.println("Ошибка записи файла: " + e.getMessage());
        }
    }
}