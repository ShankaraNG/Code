/*Q Given an array rotate or shift by N numbers
[12, 23, 25, 26, 56]
Enter the postion to which you want to rotate
2
[56, 12, 23, 25, 26]
*/

package practice;

import java.util.Arrays;
import java.util.Scanner;

public class array_rotate_no {

	public int[] rotate(int[] a, int p, int k) {

		if(p!=k) {

			int last = a[a.length - 1]; 
			for (int i = a.length - 1; i > 0; i--) {
				a[i] = a[i - 1];
			}

			a[0] = last;
			p++;
			return rotate(a,p,k);
		}
		else {
			return a;
		}
	}
	
	public static void main(String[] args) {
		int[] n = {12,23,25,26,56};
		System.out.println(Arrays.toString(n));
		array_rotate_no b = new array_rotate_no();
		System.out.println("Enter the postion to which you want to rotate");
		Scanner s = new Scanner(System.in);
		int num = s.nextInt();
		int[] c = b.rotate(n, 0, num-1);
		System.out.println(Arrays.toString(c));
	}

}
