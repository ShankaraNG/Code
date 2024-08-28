package practice;

import java.util.Arrays;


public class Binary_Search {



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


	public int brinarysearch(int a[] , int num) {
		int i = -1;
		int len = a.length;
		for (i = 0; i < len; i++) {

			if(a[i] > num && a[len] < num) {
				if (a[len/2] > num || a[len/2] == num ) {
					i = len/2-1;
					len = len/2;
				}
				else if(a[len/2] < num || a[len/2] == num ) {
					len = len/2;
				}
				else {
					continue;
				}
			}
			
			if(a[i] == num) {
				break;
			}
		}
		return i;
	}
	


	public static void main(String[] args) {

		int[] ob = {10,40,30,100,20,40};
		Binary_Search bo = new Binary_Search();
		System.out.println(Arrays.toString(ob));
		int[] b = bo.min(ob);
		System.out.println(Arrays.toString(b));
		int a = bo.brinarysearch(b,100);
		System.out.println("The position is " + a);


	}
}
