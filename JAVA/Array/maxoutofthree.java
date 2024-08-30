/*Q you are given an array of integers arr and an integer K your task is to find and print the maximun number
in each contiguous windows of size 3
example
{1,3,-1,-3,5,-3,6,7};
[3, 3, 5, 5, 6, 7]*/
		
package practice;

import java.util.Arrays;

public class maxoutofthree {
	
	public int[] max(int[] a) {
		int m;
		int[] ma = new int[a.length-2];
		for (int i = 0; i < a.length-2; i++) {
			m = Integer.max(Integer.max(a[i], a[i+1]), a[i+2]);
			ma[i] =m;
		}
		
		return ma;

	}
	
	public static void main(String[] args) {
		maxoutofthree obj = new maxoutofthree();
		int[] a = {1,3,-1,-3,5,-3,6,7};
		int[] b = obj.max(a);
		System.out.println(Arrays.toString(b));
		
	}

}
