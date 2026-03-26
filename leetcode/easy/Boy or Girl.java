import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Read input string
        String input = sc.nextLine();

        // Array to count presence of each letter (a-z)
        int[] letters = new int[26];

        // Count occurrences of each character
        for (char c : input.toCharArray()) {
            letters[c - 'a']++;
        }

        // Convert counts to binary presence (0 or 1)
        // 1 if the letter appears at least once
        for (int i = 0; i < 26; i++) {
            if (letters[i] != 0) {
                letters[i] = 1;
            }
        }

        // Count number of distinct characters
        int distinctCount = 0;
        for (int val : letters) {
            distinctCount += val;
        }

        // If number of distinct characters is even -> "CHAT WITH HER!"
        // Otherwise -> "IGNORE HIM!"
        if (distinctCount % 2 == 0) {
            System.out.println("CHAT WITH HER!");
        } else {
            System.out.println("IGNORE HIM!");
        }

        sc.close();
    }
}
