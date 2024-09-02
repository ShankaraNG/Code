/*Q given a number C, check if a2+b2=c
example
c=5
output =true
1*1 + 2*2 = 5
*/
package practice;

import java.util.Scanner;

public class sumofsquarenumber {

	public boolean sumofsquarenum(int a) {
		int num;
		boolean flag = false;
		for (int i = 1; i <a; i++) {
			num = a-(i*i);
			int j;
			for (j = 1; j < a; j++) {
				if (num==(j*j)) {
					flag =true;
					break;
				}
			}
			if (flag) {
				break;
			}
		}

		return flag;

	}

	public static void main(String[] args) {
		sumofsquarenumber obj = new sumofsquarenumber();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number");
		int a = sc.nextInt();
		System.out.println(obj.sumofsquarenum(a));
	}

}
