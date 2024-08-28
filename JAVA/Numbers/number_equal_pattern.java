/*Q given an even interger n print the following pattern
if n =8
87777778
87666678
87655678
87655678
87666678
87777778
88888888*/


package practice;

import java.util.Scanner;

public class number_equal_pattern {

	public void print(int n) {

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {

				int minDistance = Math.min(Math.min(i, j), Math.min(n - i - 1, n - j - 1));
				System.out.print((n - minDistance));
			}
			System.out.println(); 
		}
	}

	public static void main(String[] args) {
		number_equal_pattern obj = new number_equal_pattern();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the Starting pattern Number");
		int n = sc.nextInt(); 
		if (n % 2 != 0) {
			System.out.println("n must be an even number.");
		}
		else {
			obj.print(n);
		}
	}
}
