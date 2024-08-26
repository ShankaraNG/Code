/*program to print the following pattern 
if a character is followed by the number next to it, it will print the number that many times
b3c3
bbbccc*/


package practice;

import java.util.Scanner;

public class pattern_num {

	public void nu(String a) {
		int len = a.length();
		char[] b = a.toCharArray();
		String[] stringArray = a.split("");
		String s = "";

		for (int i = 0; i < len-1; i++) {

			if (Character.isLetter(b[i])) {

				String S1 = String.valueOf(b[i]);
				int num1=0;
				for (int j = i+1; j < len; j++) {
					if (Character.isLetter(b[j])) {
						break;
					}
					else {
						int num = Integer.parseInt(stringArray[j]);
						num1=num1*10 + num;
					}
				}
				
				for (int j = 1; j < num1; j++) {
					S1=S1+b[i];

				}

				s = s+S1;


			}

		}

		System.out.println(s);

	}

	public static void main(String[] args) {
		pattern_num a = new pattern_num();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the string");
		String p = sc.next();
		String per = p.trim();
		a.nu(per);
	}

}
