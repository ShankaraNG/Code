package practice;

import java.util.Scanner;

public class factorial_num {
	
	public int factorial(int num, int fac) {
		if(num==0) {
			return 1;
		}
		else if(fac>0) {;
			num = num*fac;
			return factorial(num, --fac);
			
		}
		else {
			return num;
		}

	}
	
	public static void main(String[] args) {
		
		factorial_num obj = new factorial_num();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number for which the factorial needs to be calculated");
		int num = sc.nextInt();
		int fac = num-1;
		int num1 = obj.factorial(num, fac);
		System.out.println("the factorial of number " + num + " is " + num1);
	}

}
