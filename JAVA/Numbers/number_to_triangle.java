/*Q write the program to print the below pattern
if n = 6
  1 7 12 16 19 21  
  2 8 13 17 20  
3 9 14 18  
4 10 15  
5 11  
6  */

package practice;

import java.util.Scanner;

public class number_to_triangle {
	
	public void print(int n) {
		int row = n;
		int col = n;
		int num;
		
		for (int i = 0; i < row; i++) {
			if (i<row/2-1) {
				System.out.print("  ");
			}
			num = i+1;
			for (int j = 0; j < col; j++) {
				if (j==col-i) {
					break;
				}
				else {
					System.out.print(num + " ");
					num+=n-j;
				}

			}
			System.out.println(' ');
		}

	}
	
	public static void main(String[] args) {
		number_to_triangle obj = new number_to_triangle();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the Muliple number");
		int n = sc.nextInt();
		obj.print(n);
	}

}
