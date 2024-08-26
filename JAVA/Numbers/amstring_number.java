/*Amstring number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
number=153
cube of each digit is 1,125,27
sume is 1+125+27 = 153 which is the original number*/
package practice;

import java.util.Scanner;

public class amstrong_number {
	
	int temp = 1;
	
	public int recur(int a, int b, int ori) {
		if(b>0) {
			a=a*ori;
			return recur(a, --b, ori);
		}
		else
		{
			return a;
		}

	}
	
	public int check(int num, int temp) {
		
		if(num>0) {
		int rem = num%10;
		int new1 = recur(rem, 2, rem);
		temp = temp + new1;
		return check(num/10, temp);
		}
		else {
			return temp;
		}
		
	}
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number for which the amstrong number needs to be calculated");
		int a =sc.nextInt();
		amstrong_number ob = new amstrong_number();
		int b = ob.check(a,0);
		if (a==b) {
			
			System.out.println("The number is Amstrong");
			
		}
		else {
			System.out.println("The number is not amstrong");
		}
		
		
	}

}
