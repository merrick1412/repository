import java.util.Random;

public class Two_D_Array {
    public static void main(String[] args) {
        int [][]testArray = new int[6][4];

        Random random = new Random();
        for (int i = 0; i < 5; i++){
            for (int x = 0; x < 3; x++){
                testArray[i][x] = random.nextInt();
            }
        }

        for (int i = 0; i< 5; i++){
            int sum = 0;
            for (int x = 0; x < 3; x++){
                sum += testArray[i][x];
            }
            testArray[i][3] = sum;
        }

        for (int i = 0; i< 3; i++){
            int sum = 0;
            for (int x = 0; x< 5; x++){
                sum += testArray[x][i];
            }
            testArray[5][i] = sum;
        }

        for (int i = 0; i < 6; i++){
            for (int x = 0; x < 4; x++){
                System.out.printf("%3d " , testArray[i][x]);
            }
            System.out.println();
        }
    }
}