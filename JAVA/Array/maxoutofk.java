/*Q you are given an array of integer arr and an integer k your task is to find and print the maximun 
number in each contiguous windows of size k
example
The given Array is[1, 5, -6, -8, 7, 8, 9, -5, -10, 10]
k=4
[5, 7, 8, 9, 9, 9, 10]*/

package practice;

import java.util.Arrays;
import java.util.Scanner;

public class maxoutofk {
	public int[] max(int[] a,int it, int k, int[] ma) {
		int max;
		if (it<a.length-k+1) {
			int m = a[it];
			
			for (int i = it; i < it+k-1; i++) {
				max = Integer.max(a[i],a[i+1]);
				if (max>m) {
					m=max;
				}
			}
			ma[it] = m;
			it+=1;
			return max(a, it, k, ma);
		}
		else {
			return ma;
		}


	}

	public static void main(String[] args) {
		maxoutofk obj = new maxoutofk();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the size of the array");
		int size = sc.nextInt();
		int[] a = new int[size];
		System.out.println("Enter the Elements to the array");
		for (int i = 0; i < a.length; i++) {
			a[i] = sc.nextInt();
		}
		System.out.println("The given Array is" + Arrays.toString(a));
		System.out.println("Enter the K element to check the highest number");
		int k = sc.nextInt();
		int[] ma = new int[a.length-k+1];
		int[] b = obj.max(a,0,k,ma);
		System.out.println(Arrays.toString(b));

	}
}
