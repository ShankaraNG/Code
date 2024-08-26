/*if the last digit of the number matches with the square of the number then it is called as
automorphic number
example num =3
num2 = 9
num is not equal to num2 hence it is not an automorphic number*/

package practice;

import java.util.Scanner;

public class peterson_number {
	
	public void peterson_number(long a){
		
		long temp = a;
		long length = 0;
		for (long i =temp; i>0;i =i/10)
		{
			length++;
		}
		length=length-1;
		long num =1;
		for (long i =1; i<=length/2;i++)
		{
			num = num * 10;

		}
		long newtemp = temp%num;
		long length1 =1;
		long temp2 = a*a;
		for (long i =temp2; i>0;i =i/10)
		{
			length1++;
		}
		length1=length1-1;
		long num1 =1;
		for (long i =1; i<=length/2;i++)
		{
			num1 = num1 * 10;

		}
		long newtemp2 = temp2%num1;
		
		if(newtemp == newtemp2) {
			System.out.println("it is a automorphic number");
		}
		else {
			System.out.println("it is not an automorphic number");
		}
		
		
	}
	
	public static void main(String[] args) {
		peterson_number ob = new peterson_number();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number to check automorphic");
		long num = sc.nextLong();
		ob.peterson_number(num);
	}

}
