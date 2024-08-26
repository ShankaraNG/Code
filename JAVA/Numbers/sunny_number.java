/*Sunny number is a number in which the given number is incremented by 1 post which if its a perfect squareroot
then its a sunny number
example
num =35
new number = 35 + 1
sqareroot of 36 = 6
which is a perfect number and hence a sunny number*/


package practice;

import java.util.Scanner;

public class sunny_number {

	public long squarerootdriver(long num) {

		long i;
		boolean flag = false;
		for (i = 1; i <=num; i++) {

			long mul = i * i;

			if (mul == num) {
				flag = true;
			}

			if (mul > num) {
				break;
			}
		}

		if (flag) {

			return i;
		}
		else {

			return 0;
		}

	}

	public static void main(String[] args) {
		
		System.out.println("Enter the number to check sunny number");
		Scanner sc = new Scanner(System.in);
		Long ob = sc.nextLong();
		ob++;
		sunny_number ob1 = new sunny_number();
		long num = ob1.squarerootdriver(ob);

		if (num == 0) {

			System.out.println("Not a sunny number");

		}
		else {
			System.out.println("The number is a sunny number");
		}


	}

}
