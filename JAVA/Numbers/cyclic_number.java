/*A cyclic number is an integer for which cyclic permutations of the digits are successive integer multiples of the number. The most widely known is the six-digit number 142857, whose first six integer multiples are

142857 × 1 = 142857
142857 × 2 = 285714
142857 × 3 = 428571
142857 × 4 = 571428
142857 × 5 = 714285
142857 × 6 = 857142
*/

package practice;

import java.util.Scanner;

public class cyclic_number {


	public void cyclic(long num) {
		long temp=num;
		int count = 0;
		for (int i = 2; i <=10; i++) {
			long mul=temp*i;
			String stro = Long.toString(temp);
			int lo = stro.length();
			String strm = Long.toString(mul);
			int lm = strm.length();
			long rem = 0;
			long runn=1;
			long temp1=0;
			long temp2=0;
			long temp0=mul;
			for (int j = 1; j < lo; j++) {
				runn=runn*10;
			}
			if (lo==lm) {
				for (int k = 1; k <= lo; k++) {
					
					rem = temp0%10;
					temp1=temp0/10;
					temp2=rem*runn + temp1;
					temp0=temp2;
					if(temp2==temp) {
						count++;
						break;
					}
				}
			}
			
		}
		
		if (count>=3) {
			System.out.println("The number " + num + " is cyclic");
		}

	}
	
	
	public void number_iteration(long a, long b) {
		if (a == 0) {
			a = a+1;
		}
		for (long i = a; i <=b; i++) {
			
			cyclic_number ob1 = new cyclic_number();
			ob1.cyclic(i);
			
		}

	}
	
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter the starting number");
		long a = scan.nextLong();
		System.out.println("Enter the Ending number");
		long  b = scan.nextLong();
		cyclic_number ob = new cyclic_number();
		ob.number_iteration(a, b);
		//ob.cyclic(142856);
			
	}

}
