/*Q to rotate the array by one element or to shift the given array by one element
example
[12, 23, 25, 26, 56]

output
		
[56, 12, 23, 25, 26]*/
		
package practice;
import java.util.Arrays;

public class array_rotate_1 {

		
		public int[] rotate(int[] a) {
			int[] ne = new int[a.length];
			for (int i = 0, j=i+1; i < a.length-1; i++,j++) {
				if (j!=a.length-1) {
					ne[j] = a[i];
				}
				else {
					ne[0] = a[a.length-1];
					ne[j] = a[i];
					
				}
			
			
			}
			
			
			return ne;

		}
		
		public static void main(String[] args) {
			array_rotate_1 b = new array_rotate_1();
			int[] n = {12,23,25,26,56};
			System.out.println(Arrays.toString(n));
			int[] c = b.rotate(n);
			System.out.println(Arrays.toString(c));
			
		}



}

