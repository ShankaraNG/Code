/*Q given an array find out the missing number and also the repeating numbers in an array
example
input n =2 array a = {2,2}
output 2 and 1
*/

package practice;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Map.Entry;

public class missingandrepeation {
	
	public ArrayList<Integer> repeating(int[] a) {
		HashMap<Integer, Integer> n = new HashMap<Integer, Integer>();
		ArrayList<Integer> fin = new ArrayList<Integer>();
		for (int i = 0; i < a.length; i++) {
			if (n.containsKey(a[i])) {
				n.put(a[i], n.get(a[i])+1 );
			}
			else {
				n.put(a[i],1);
			}
		}
		
		for (Entry<Integer, Integer> entry : n.entrySet()) {
			Integer key = entry.getKey();
			Integer val = entry.getValue();
			if (val>=2) {
				fin.add(key);
			}
		}
		
		return fin;

	}
	
	public ArrayList<Integer> missing(int[] a) {
		ArrayList<Integer> fin = new ArrayList<Integer>();
		
		for (int i = a.length; i > 0; i--) {
			boolean flag =true;
			for (int j = 0; j < a.length; j++) {
				if (i==a[j]) {
					flag =false;
					break;
				}
			}
			if (flag) {
				fin.add(i);
			}
			
		}
		
		return fin;

	}
	
	public static void main(String[] args) {
		missingandrepeation obj = new missingandrepeation();
		System.out.println("Enter the size of the array");
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		System.out.println("Enter the digits into the array");
		for (int i = 0; i < a.length; i++) {
			a[i]=sc.nextInt();
		}
		ArrayList<Integer> mis = obj.missing(a);
		ArrayList<Integer> rep = obj.repeating(a);
		
		System.out.println("The missing numbers are " + mis.toString());
		System.out.println("The repeatingnumbers are " + rep.toString());
	}

}
