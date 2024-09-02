/*Q given a string convert the letters by interchanging the given letters to form a secret message
for example
input apple
ch 1 = a
ch 2 = p
output paale*/

package practice;


import java.util.Scanner;

public class secretmessage {
	
	public String message(String S,char x,char y) {
		char [] a = S.toCharArray();
	
		for (int i = 0; i < a.length; i++) {
			if (a[i]==x) {
				a[i]=y;
			}
			else if (a[i]==y) {
				a[i]=x;
			}
			else {
				continue;
			}
		}
		
		String f = new String(a);
		return f;
	}
	
	public static void main(String[] args) {
		secretmessage ob = new secretmessage();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the string to be converted into a secret message");
		String s = sc.next();
		System.out.println("Enter the two characters to be interchanged");
		char x = sc.next().charAt(0);
		char y = sc.next().charAt(0);
		String f =  ob.message(s, x, y);
		System.out.println("The secret message is");
		System.out.println(f);
		
	}

}
