/*Q Write a function that takes an interger n as input and returns the 
sum of all the prime numbers less than n
input 10
output = 17
explanation 2+3+5+7 = 17*/

package practice;

import java.util.Scanner;

public class sumoflessprime {

	public int prim(int n) {
		int sum = 0;
		//calculating the prime number
		for (int i = n-1; i > 1; i--) {
			boolean flag = true;
			for (int j2 = 2; j2 <= i/2; j2++) {

				if (i%j2==0) {
					flag =false;
					break;
				}

			}
			//if its a prime then add it to the sum or else continue the execution
			if (flag) {
				sum=sum+i;
			}

		}

		return sum;

	}

	public static void main(String[] args) {
		sumoflessprime obj = new sumoflessprime();
		System.out.println("Enter the number");
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int n = obj.prim(a);
		if (n!=0) {
			System.out.println("The sum of the prime numbers less than the given number is " + n);
		}
		else {
			System.out.println("The given number has no prime numbers less than it");
		}
	}

}
