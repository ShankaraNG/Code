package practice;

import java.util.Arrays;

public class selection_sort {

	public int[] min(int[] a) {
		
		int temp2;

		for (int i = 0; i < a.length-1; i++) {
			int temp = i;
			for (int j = i+1; j < a.length; j++) {
				if (a[j] < a[temp]) {
					temp = j;
				}
			}
			
			if (temp != i) {
				temp2 = a[i];
				a[i] = a[temp];
				a[temp] = temp2;
				temp = a[i];
			}
			
		}


		return a;

	}


	public static void main(String[] args) {

		int[] ob = {10,40,30,100,20,40};
		selection_sort bo = new selection_sort();
		System.out.println(Arrays.toString(ob));
		int[] b = bo.min(ob);
		System.out.println(Arrays.toString(b));


	}
}
