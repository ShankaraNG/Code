/*A spy number is a number in which the numbers are first separated and in the first case it is added internally
and second it is multiplied internally and if the sum matches the product then it is Spy number
example
number - 321
sum = 3+2+1
product = 3*2*1
if sum == product then it is a spy number*/

package practice;

import java.util.Scanner;

public class spy_number {
	
	public long sum(long num) {
		long sum = 0;
		
		for (long i = num; i > 0; i = i/10) {
			
			sum = sum + (i%10);
			
		}
			return sum;

	}
	
	public long prod(long num) {
		long prod = 1;
		
		for (long i = num; i > 0; i = i/10) {
			
			prod = prod * (i%10);
			
		}
			return prod;

	}
	
	public String checker(long num) {
		
		long ob = sum(num);
		long ob1 = prod(num);
		
		if (ob == ob1) {
			return "is a spy number";
		}
		else {
			return "is not a spy number";
					
		}
	}
	
	public static void main(String[] args) {
		System.out.println("Enter the Spy number");
		Scanner sc = new Scanner(System.in);
		Long ob = sc.nextLong();
		spy_number ob1 = new spy_number();
		String a = ob1.checker(ob);
		System.out.println(a);
		
	}

}
