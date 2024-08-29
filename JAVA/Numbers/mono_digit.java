/*check if you can convert a given number to mono digit or not
for example
72581
The number can be converted to MONO digit
777*/

package practice;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class mono_digit {
	
	public void check(int a) {
		String s = Integer.toString(a);
		int[] ori = new int[s.length()];
		
		for (int i = s.length()-1; i >= 0 && a>0; i--,a= a/10) {
			ori[i] = a%10;
		}
		
		ArrayList<Integer> ar = new ArrayList<Integer>();
		ar.add(ori[0]);
		for (int i = 1; i < ori.length-1; i++) {
			
			int sum = ori[i] + ori[i+1];
			int diff = ori[i] - ori[i+1];
			
			if (ori[0]==sum) {
				ar.add(sum);
			}
			
			if (ori[0]==diff) {
				ar.add(diff);
			}
			
		}
		
		boolean flag = true;
		
		
		Iterator<Integer> i = ar.iterator();
		StringBuffer s1 = new StringBuffer();
		
		for (Integer integer : ar) {
			if (!integer.equals(ori[0])) {
				flag = false;
			}
			else {
				s1.append(integer);
			}
			
		}
		if (flag) {
			System.out.println("The number can be converted to MONO digit");
			System.out.println(s1);
		}
		else {
			System.out.println("The given number cannot be converted to MONO digit");
		}

	}
	
	
	public static void main(String[] args) {
		mono_digit obj = new mono_digit();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number to check if it can be converted to mono digit or not");
		int a = sc.nextInt();
		obj.check(a);
	}
}
