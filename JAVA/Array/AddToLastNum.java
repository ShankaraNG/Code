/*Q add 1 number to the last iteration of the array
for example
a =[1,2,3]
output = [1,2,4]
if in case you get 9
it should a 1 to the next number
a= [9]
output = [1,0]
if a [7,9,9]
output [8,0,0]*/


package practice;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class AddToLastNum {

	public List<Integer> add(int[] a) {
		ArrayList<Integer> n = new ArrayList<Integer>();
		int count =0;

			for (int i = a.length-1; i >=0; i--) {
				if (a[i]==9&& (i == a.length-1) && a.length!=1) {
					n.add(0);
					count=1;
				}
				else if (count==1 && (i != a.length-1) && i!=0 && a[i] == 9) {
					n.add(0);
				}
				else if (count==1 && (i != a.length-1) && a[i] != 9) {
					n.add(a[i]+1);
					count = 0;
				}
				else if(i == a.length-1 && a[i]!=9 ) {
					n.add(a[i]+1);
				}
				else if((i == 0 && a[i]==9 && count==1 )|| (i == 0 && a[i]==9 && a.length==1 ) ) {
					n.add(0);
					n.add(1);
					count =0;
				}
				else {
					n.add(a[i]);
				}

			}

		return n.reversed();

	}

	public static void main(String[] args) {
		AddToLastNum obj = new AddToLastNum();
		System.out.println("Enter the size of the array");
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		System.out.println("Enter the digits into the array");
		for (int i = 0; i < a.length; i++) {
			a[i]=sc.nextInt();
		}
		List<Integer> fin = obj.add(a);
		System.out.println(fin);
	}

}
