package practice;

import java.util.Scanner;

public class linearsearch_array {
	
	public int search(int[] a, int c) {
		int j = -1;
		for (j = 0; j < a.length; j++) {
			int b = a[j];
			if(b == c) {
				break;
			}
		}
		
		return j;

	}
	
	
	
	public static void main(String[] args) 
	{
		int[] ob = new int[4];
		for (int i = 10, j = 0; j < ob.length; i+=10, j++) {
			ob[j] = i;
		}
		
		linearsearch_array a = new linearsearch_array();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number to be searched in the array");
		int b =sc.nextInt();
		int c = a.search(ob, b);
		if (c!=-1) {
			System.out.println("The element exists in the position " + c);
		}
		else {
			System.out.println("The element does not exists");
		}

	}

}
