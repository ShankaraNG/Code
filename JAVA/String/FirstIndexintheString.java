package practice;

import java.util.Scanner;

public class FirstIndexintheString {
	
	
	public String[] stringsplitter(String a) {
		String [] b = a.split("");
		return b;
	}
	
	public int firststringdrive(String a, String b) {
		
		String[] main = a.split(" ");
		String[] findstring = stringsplitter(b);
		int index = -1;
		for(int i =0;i<main.length;i++) {
			String temp = main[i];
			String[] temparray = stringsplitter(temp);
			boolean flag = false;
			if(temparray.length == findstring.length) {
				flag = true;
				for(int j = 0; j<temparray.length; j++) {
					if(!temparray[j].equals(findstring[j])) {
						flag = false;
						break;
					}
					
				}
			}
			
			if(flag) {
				index = i;
				break;
			}			
			
		}
		
		return index;
	}
	
	public static void main(String[] args) {
		
		FirstIndexintheString obj = new FirstIndexintheString();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the first String");
		String main = sc.nextLine();
		System.out.println("Enter the matching String");
		String match = sc.nextLine();
		if(main == null || match == null) {
			System.out.println("Invalid Input for the First String or the matching String");
		}
		else {
			int value = obj.firststringdrive(main, match);
			if(value>=0) {
				System.out.println("A Match has been found for the string " + match + " and its first occurancy is placed at "+ value);
			}
			else {
				System.out.println("No Match has been found for the string " + match);
			}
		}
	}

}
