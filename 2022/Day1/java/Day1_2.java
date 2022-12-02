// ================
// Part 2
// ================

// ZhengLinLei



import java.util.Scanner;  // Import the Scanner class
import java.io.*;  
import java.util.Arrays;


public class Day1_2 {
    public static final String FILENAME = "../input.txt";
    private static int[] input = {};
    private static int[][] total = {};
    private static int[] max = {};
    public static boolean isStringInt(String s) {
        try
        {
            Integer.parseInt(s);
            return true;
        } catch (NumberFormatException ex)
        {
            return false;
        }
    }

    public static int[] push(int[] array, int push) {
        int[] longer = new int[array.length + 1];
        for (int i = 0; i < array.length; i++)
            longer[i] = array[i];
        longer[array.length] = push;
        return longer;
    }

    public static int[][] pushArr(int[][] array, int[] push) {
        int[][] longer = new int[array.length + 1][];
        for (int i = 0; i < array.length; i++)
            longer[i] = array[i];
        longer[array.length] = push;
        return longer;
    }

    public static void main(String[] args) throws IOException {
        try {
            File myfile = new File(FILENAME);
            Scanner openfile = new Scanner(myfile);

            while (openfile.hasNextLine()) {

                String filedata = openfile.nextLine();
                if(isStringInt(filedata)) {

                    input = push(input, Integer.parseInt(filedata));
                }else{
                    total = pushArr(total, input);
                    input = new int[0];
                }
            }
            openfile.close();

            // Print out the array
            for (int i = 0; i < total.length; i++) {
                int x = 0;
                for (int j = 0; j < total[i].length; j++) {
                    System.out.print(total[i][j] + " ");
                    x += total[i][j];
                }
                System.out.println();
                max = push(max, x);
            }

            System.out.println("Max: " + Arrays.toString(max));
            
            int[] max2 = {};
            // Foreach max array and find the max
            // Then change the int to 0
            // Then find the next max
            // Then change the int to 0

            for (int i = 0; i < 3; i++) {
                int max1 = 0;
                for (int j = 0; j < max.length; j++) {
                    if(max[j] > max1) {
                        max1 = max[j];
                        max[j] = 0;
                    }
                }
                max2 = push(max2, max1);
                System.out.println("Max2: " + Arrays.toString(max2));
            }

            // Sum max2 item
            int totalTop = 0;
            for (int i = 0; i < max2.length; i++) {
                totalTop += max2[i];
            }

            System.out.println("MaxTotal{Top:3}: " + totalTop); // [64929, 64078, 63931]
        } catch (FileNotFoundException e) {
            System.out.println("Error.");
            e.printStackTrace();
        }
    }
}
