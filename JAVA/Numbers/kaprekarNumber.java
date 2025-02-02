/*
The Kaprekar constant is a special number that arises from a process involving the manipulation of the digits of a number. The most famous Kaprekar constant is 6174, which is the result of a procedure known as Kaprekar's routine.

How Kaprekar's Routine Works:
Pick any four-digit number where at least two digits are different. (If all digits are the same, the routine doesn’t work.)

Arrange the digits in descending order to form the largest possible number and then in ascending order to form the smallest possible number.

Subtract the smaller number from the larger number.

Repeat the process with the result from the previous step.

Example with 3524:
Take the number 3524.
Largest number from the digits: 5432.
Smallest number from the digits: 2345.
Subtract: 5432 - 2345 = 3087.
Now, repeat the process with 3087:

Largest number: 8730.
Smallest number: 0378 (which is 378).
Subtract: 8730 - 378 = 8352.
Repeat again with 8352:

Largest number: 8532.
Smallest number: 2358.
Subtract: 8532 - 2358 = 6174.
After just a few steps, we reach 6174. Once you reach 6174, repeating the process will always give 6174.

below is the list of example

Enter the starting four digit number
1000
Enter the ending four digit number
9999
Below is the list of numbers which do not adhere to karpekar rule are 
[1000, 1011, 1101, 1110, 1111, 1112, 1121, 1211, 1222, 2111, 2122, 2212, 2221, 2222, 2223, 2232, 2322, 2333, 3222, 3233, 3323, 3332, 3333, 3334, 3343, 
 3433, 3444, 4333, 4344, 4434, 4443, 4444, 4445, 4454, 4544, 4555, 5444, 5455, 5545, 5554, 5555, 5556, 5565, 5655, 5666, 6555, 6566, 6656, 6665, 6666, 
 6667, 6676, 6766, 6777, 7666, 7677, 7767, 7776, 7777, 7778, 7787, 7877, 7888, 8777, 8788, 8878, 8887, 8888, 8889, 8898, 8988, 8999, 9888, 9899, 9989, 9998, 9999]*/



package practice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class kaprekarNumber {

	public long highOrder(long a) {
		String numberStr = Long.toString(a);
		char[] b = numberStr.toCharArray();
		int[] c = new int[b.length];

		for (int i = 0; i < b.length; i++) {
			int number = Character.getNumericValue(b[i]);
			c[i] = number;
		}

		// Sorting array in descending order
		Arrays.sort(c); // Sort in ascending order by default
		int[] reversed = new int[c.length];
		for (int i = 0; i < c.length; i++) {
			reversed[i] = c[c.length - 1 - i]; // Reverse for descending order
		}

		StringBuilder sb = new StringBuilder();
		for (int digit : reversed) {
			sb.append(digit);
		}

		long rno = Long.parseLong(sb.toString());
		return rno;
	}

	public long lowerOrder(long a) {
		String numberStr = Long.toString(a);
		char[] b = numberStr.toCharArray();
		int[] c = new int[b.length];

		for (int i = 0; i < b.length; i++) {
			int number = Character.getNumericValue(b[i]);
			c[i] = number;
		}

		// Sorting array in ascending order
		Arrays.sort(c); // Sort in ascending order by default

		StringBuilder sb = new StringBuilder();
		for (int digit : c) {
			sb.append(digit);
		}

		long rno = Long.parseLong(sb.toString());
		return rno;
	}

	public int driver(long a) {

		long temp = a;
		long temp1 = temp;
		String s = Long.toString(temp);
		int length = s.length();
		long num = 6174;
		long check = 0;
		boolean flag = false;
		while (check != num) {
			long HO = highOrder(temp1);
			long LO = lowerOrder(temp1);
			temp1 = HO - LO;
			if (HO == LO || temp1 == 0) {
				break;
			}
			check = temp1;
			if (check == num) {
				flag = true;
				break;
			}
		}
		int rn = 0;
		if (!flag) {
			rn = (int) temp;
		}

		return rn;
	}

	public ArrayList<Integer> drivermain(long a, long b) {
		ArrayList<Integer> al = new ArrayList<Integer>();
		for (long i = a; i <= b; i++) {
			int c = driver(i);
			if (c != 0) {
				al.add(c);
			}
		}

		return al;

	}

	public static void main(String[] args) {

		kaprekarNumber ob = new kaprekarNumber();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the starting four digit number");
		long a = sc.nextLong();
		System.out.println("Enter the ending four digit number");
		long b = sc.nextLong();
		String num1 = Long.toString(a);
		String num2 = Long.toString(b);
		if (num1.length() != 4 || num2.length() != 4) {
			System.out.println("Enter the correct values");
		} else {
			ArrayList<Integer> al = new ArrayList<Integer>();
			al = ob.drivermain(a, b);
			if (al.isEmpty()) {
				System.out.println("All the number between " + a + " and " + b + " adhere to Karpekar constant rule");
			} else {
				System.out.println("Below is the list of numbers which do not adhere to karpekar rule are ");
				System.out.println(al);
			}
		}
	}

}
