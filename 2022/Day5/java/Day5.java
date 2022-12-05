// Part 1
// ================

// ZhengLinLei

import java.io.*;

public class Day5 {

    public static String[] columns = new String[10];

    public static void main(String[] args) {
        String filename = "./2022/Day5/input.txt";
        BufferedReader reader;
        String line = "";
        try {
            reader = new BufferedReader(new FileReader(filename));
            line = reader.readLine();
            for (int i = 0; i < columns.length; i++) {
                columns[i] = "";
            }

            while (line != null && !line.contains("move")) {
                addrow(line);
                line = reader.readLine();
            }

            for (int i = 0; i < columns.length; i++)
                columns[i] = flipString(columns[i]);

            while (line != null) {

                if (line.split(" ").length >= 5) {
                    int quantity = Integer.parseInt(line.split(" ")[1]);
                    int from = Integer.parseInt(line.split(" ")[3]) - 1;
                    int to = Integer.parseInt(line.split(" ")[5]) - 1;
                    // PART 1
                    for (int j = 0; j < quantity; j++)
                        moveElement(from, to);
                    // PART 2
                    // moveElements(from,to,quantity);
                }

                line = reader.readLine();

            }
            printTop();
        } catch (Exception e) {
            System.out.println("PROBLEM" + e);
        }

    }

    public static void addrow(String input1) {

        if (input1.length() >= 3) {
            int numColumns = (input1.length() + 1) / 4;
            for (int i = 0; i < numColumns; i++) {
                columns[i] = columns[i] + input1.charAt(i * 4 + 1);
            }
        }

    }

    public static String flipString(String s) {
        String Stringflip = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) != ' ')
                Stringflip = Stringflip + s.charAt(i);
        }
        return (Stringflip);
    }

    public static void printTop() {
        for (int i = 0; i < 10; i++)
            if (columns[i].length() > 0)
                System.out.print(columns[i].charAt(columns[i].length() - 1));

    }

    public static void moveElement(int from, int to) {
        char c = columns[from].charAt(columns[from].length() - 1);
        columns[from] = columns[from].substring(0, columns[from].length() - 1);
        columns[to] = columns[to] + c;

    }

    public static void moveElements(int from, int to, int qty) {
        String sub1 = columns[from].substring(columns[from].length() - qty, columns[from].length());
        columns[from] = columns[from].substring(0, columns[from].length() - qty);
        columns[to] = columns[to] + sub1;

    }

}