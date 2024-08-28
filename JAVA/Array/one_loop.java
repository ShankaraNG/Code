/*Q given an array as mentioned below
[0, -1, 1, 1, 0, -1]
		
Sort it in this pattern using a single loop only
[-1, -1, 1, 1, 0, 0]
*/
package practice;

import java.util.Arrays;

public class one_loop {

	public void chec(int[] a) {

		int ab = 0;
		int b = 2;
		int c =4;
		int[] k = new int[a.length];
		for (int i = 0; i < a.length; i++) {

			if (a[i]==1) {
				k[b]=a[i];
				b++;
			}
			else if (a[i]==0) {
				k[c]=a[i];
				c++;
			} else {
				k[ab]=a[i];
				ab++;
			}



		}
		System.out.println(Arrays.toString(k));
	}

	public static void main(String[] args) {
		
		one_loop b = new one_loop();
		int[] c = {0,-1,1,1,0,-1};
		System.out.println(Arrays.toString(c));
		b.chec(c);

	}

}
