package practice;

/*To print the matrix in the form of spiral for the given input. For example if the number of rows and coloumn is 3 then the output should be
01 02 03 
08 09 04 
07 06 05 
*/
import java.util.Scanner;

public class matrixPattern {
	public void Pattern(int x, int y) {
		// Create a 2D array to store the matrix
		String[][] matrix = new String[x][y];

		// Define the boundaries for filling the matrix
		int start = 1, end = x * y;
		int left = 0, right = y - 1, top = 0, bottom = x - 1;

		// Start filling the matrix in a spiral order
		while (start <= end) {
			// Fill top row (left to right)
			for (int i = left; i <= right; i++) {
				if (start < 10) {
					String c = ("0" + start);
					matrix[top][i] = c;
					start++;

				} else {
					matrix[top][i] = String.valueOf(start);
					start++;
				}

			}
			top++;

			// Fill right column (top to bottom)
			for (int i = top; i <= bottom; i++) {
				if (start < 10) {
					String c = ("0" + start);
					matrix[i][right] = c;
					start++;

				} else {
					matrix[i][right] = String.valueOf(start);
					start++;
				}

			}
			right--;

			// Fill bottom row (right to left)
			for (int i = right; i >= left; i--) {
				if (start < 10) {
					String c = ("0" + start);
					matrix[bottom][i] = c;
					start++;

				} else {
					matrix[bottom][i] = String.valueOf(start);
					start++;
				}
			}
			bottom--;

			// Fill left column (bottom to top)
			for (int i = bottom; i >= top; i--) {
				if (start < 10) {
					String c = ("0" + start);
					matrix[i][left] = c;
					start++;

				} else {
					matrix[i][left] = String.valueOf(start);
					start++;
				}
			}
			left++;
		}

		// Print the matrix in the required format
		for (int i = 0; i < x; i++) {
			for (int j = 0; j < y; j++) {
				System.out.print(matrix[i][j] + " ");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number of rows");
		int x = sc.nextInt();
		System.out.println("Enter the number of coloumns");
		int y = sc.nextInt();

		matrixPattern a = new matrixPattern();
		try {
			a.Pattern(x, y);
		} catch (Exception e) {
			System.out.println(e);
		}

	}
}
