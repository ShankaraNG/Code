/*Q Given an array calculate the number of times the second highest number is repeated
example
1,2,3,4,4,5,5,5
output
2
explanation
number 4 is repeated twice*/


package practice;


import java.util.HashMap;
import java.util.Scanner;
import java.util.Map.Entry;

public class numofsecondoccur {

	public int count(int[] a) {
		int temp;
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a.length-i-1; j++) {
				if (a[j]>a[j+1]) {
					temp = a[j];
					a[j] = a[j+1];
					a[j+1] = temp;
				}

			}
		}

		HashMap<Integer, Integer> a1 = new HashMap<Integer, Integer>();

		for (int i : a) {
			if (a1.containsKey(i)) {
				a1.put(i,a1.get(i)+1);	
			}
			else {
				a1.put(i,1);
			}
		}

		int n = a[a.length-1];
		boolean flag = false;
		for (int i = 0; i < a.length; i++) {
			n=n-1;
			for (int j = 0; j < a.length; j++) {
				if (n==a[j]) {
					flag = true;
					break;
				}
			}
			if (flag) {
				break;
			}
		}
		int val=0;

		for (Entry<Integer, Integer> entry : a1.entrySet()) {
			int key = (int) entry.getKey();
			if (n==key) {
				val = entry.getValue();
				break;
			} 

		}
		return val;
	}

	public static void main(String[] args) {
		numofsecondoccur obj = new numofsecondoccur();
		System.out.println("Enter the size of the array");
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		System.out.println("Enter the digits into the array");
		for (int i = 0; i < a.length; i++) {
			a[i]=sc.nextInt();
		}
		int num = obj.count(a);
		System.out.println("The no of time second highest number is present in the given array of numbers is " + num);
	}

}
