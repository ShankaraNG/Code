/*Given two arrays take the individual numbers and add it to the same position of the 
other array and print the sum in ascending order
*/


package practice;

import java.util.Arrays;


public class merge_elements_sortearr {

	public int[] merger(int[] a, int[] b) {
		int[] c = new int[a.length];
		for (int i = 0,j=0; i < b.length; i++,j++) {
			c[i] = a[i] + b[i];
		}
		int temp;
		for (int i = 0;  i < c.length-1;i ++) {
			if (c[i]>c[i+1]) {
				temp = c[i];
				c[i] = c[i+1];
				c[i+1] = temp;
			}
		}

		return c;

	}

	private int[] match(int[] a, int[] b) {
		int len = a.length;
		int len1 = b.length;

		if (len>len1) {
			int[] c = new int[a.length];
			for (int i = 0; i < c.length; i++) {
				if (i<b.length) {
					c[i] = b[i];
				}
				else {
					c[i] = 0;
				}	
			}
			int[] d = merger(a, c);
			return d;
		}
		else {
			int[] c = new int[b.length];
			for (int i = 0; i < c.length; i++) {
				if (i<a.length) {
					c[i] = a[i];
				}
				else
				{
					c[i] = 0;
				}


			}
			int[] d = merger(b, c);
			return d;
		}

	}

	public static void main(String[] args) {
		merge_elements_sortearr ob = new merge_elements_sortearr();
		int[] a = {2,4,6};
		int[] b = {2,3,5,9,11};
		int[] e = ob.match(a, b);
		System.out.println(Arrays.toString(e));

	}

}
