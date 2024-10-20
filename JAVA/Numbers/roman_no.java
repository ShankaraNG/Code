/*roman numbers are represented by seven number and write a code to convert
them in to numerical value
input VIII
output 8
*/
package practice;

import java.util.HashMap;
import java.util.Scanner;
import java.util.Map.Entry;

public class roman_no {

	public int rome(String a) {

		char[] c = a.toCharArray();
		HashMap<Character, Integer> rom = new HashMap<Character, Integer>();
		rom.put('I', 1);
		rom.put('V', 5);
		rom.put('X', 10);
		rom.put('L', 50);
		rom.put('C', 100);
		rom.put('D', 500);
		rom.put('M', 1000);

		int sum = 0;

		for (int i = 0; i < c.length; i++) {
			
			char d = c[i];

			for (Entry<Character, Integer> entry : rom.entrySet()) {
				Character key = entry.getKey();
				if(d==key) {
					Integer val = entry.getValue();
					sum = sum + val;
				}

			}

		}


		return sum;

	}

	public static void main(String[] args) {

		roman_no ob = new roman_no();
		Scanner sc = new Scanner(System.in);

		System.out.println("Enter the roman number");
		String a = sc.next();
		int c = ob.rome(a);
		System.out.println("The entered roman number to numberic value is " + c);

	}
}
