/*A number is a tech number if it is first divided by the half of its length and the two separate halfs are added
together and squared if the resulting number is equal to the orginial number then its a tech number
example
num = 3025
num1=30
num2=25
num3=30+25
num4 = num3 * num3
if num4 == num then it is called as tech number*/

package practice;

import java.util.Scanner;

public class tech_number {

	public static String tecnum(int a){
		int sum =0;
		int temp = a;
		int length = 0;
		for (int i =temp; i>0;i =i/10)
		{
			length++;
		}


		if (length%2==0) {

			int num =1;
			for (int i =1; i<=length/2;i++)
			{
				num = num * 10;

			}

			int rem = a%num;
			int q0 = a/num;
			int sq1 = rem + q0;
			int sq2 = sq1 * sq1;

			if(sq2==a) {

				return "Tech";
			}
			else {
				return "not tech";
			}
		}
		else {
			return "the length of the number is not even";
		}	

	}



	public static void main(String[] args) 
	{
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter the number to check if its a tech or not");
		int a = scan.nextInt();
		String ob = tecnum(a);
		System.out.println(ob);
	}

}
