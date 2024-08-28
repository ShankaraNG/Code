package practice;

import java.util.Arrays;

public class bubble_sort {

	public int[] min(int[] a) {
		int temp;
		for (int i = 0; i < a.length-1; i++) {

			for (int j = 0; j < a.length-1-i; j++) {
				if (a[j]>a[j+1]) {
					temp = a[j];
					a[j] = a[j+1];
					a[j+1] = temp;

				}

			}

		}

		return a;

	}


	public static void main(String[] args) {

		int[] ob = {10,40,30,100,20,40};
		bubble_sort bo = new bubble_sort();
		System.out.println(Arrays.toString(ob));
		int[] b = bo.min(ob);
		System.out.println(Arrays.toString(b));


	}
}
