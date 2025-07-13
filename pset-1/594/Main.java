import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        int x;
        while(s.hasNextInt()) {
            x = s.nextInt();

            int b1 = x & 0xFF;
            int b2 = (x >> 8) & 0xFF;
            int b3 = (x >> 16) & 0xFF;
            int b4 = (x >> 24) & 0xFF;
            
            int y = (b1 << 24) | (b2 << 16) | (b3 << 8) | b4;
            if ((y & (1 << 31)) == 1)
                y = -(1 + (y ^ 0xffffffff));

            System.out.format("%d converts to %d\n", x, y); 
        }

        s.close();
    }
}
