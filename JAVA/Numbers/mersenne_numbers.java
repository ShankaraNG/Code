/*A Mersenne prime is a prime number that can be written in the form \(2^{n}-1\). For example \(31\) is a Mersenne prime that can be written as \(2^{5}-1\). The first few Mersenne primes are \(3, 7, 31, 127, 8191\). There are 50 known Mersenne primes as of June 2018, though we hope that it will change in the future. An interesting thing about Mersenne primes is that
they are the easiest natural numbers to prove to be primes, so they make up the largest category on the list of known prime numbers
*/

package practice;

import java.util.Scanner;

public class mersenne_numbers {
	
	public long mersenne(long num) {
		long mul = 2;
		for (int i = 1; i <num; i++) {
			mul = mul *2;
		}
		
		long mur = mul -1;
		boolean flag = true;
		for (long i = 2; i <=mur/2; i++) {
			if (mur%i==0) {
				flag = false;
				break;
			}
		}
		
		if (flag) {
			return mur;
		}
		else {
			return 0;
		}

	}
	
	public void mersenne_driver(long start, long end) {
		if (start==0) {
			start = start +1;
		}
		for (long i = start; i <= end; i++) {
			
			long a = mersenne(i);
			if(a!=0) {
				System.out.println("The number " + i + " is a mersenne number as 2^" + i + "-1=" + a);
			}
			
		}

	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the Starting number");
		long a =sc.nextLong();
		System.out.println("Enter the Ending number");
		long b =sc.nextLong();
		mersenne_numbers ob = new mersenne_numbers();
		ob.mersenne_driver(a, b);
	}

}
