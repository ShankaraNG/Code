/*Q given an input string abc to print all the permutation and combination of the string for example
input=>abc
output=>
a
b
c
ab
ac
ca
cb
bc
ba
abc
bac
cab
cba*/



package practice;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;

public class comboPattern {
	
	public LinkedList<String> patternappend(String s) {
		String t=s;
		int countx=1;
		int l =t.length();
		String[] ca = t.split("");
		LinkedList<String> hm = new LinkedList<String>();
		if (countx<=l) {
			for (int i = 0; i < ca.length; i++) {
				
				if(!hm.contains(ca[i])) {
					hm.add(ca[i]);
				}
			}
			countx++;
		} else {
			return hm;
		}
		
		
		
		if (countx<=l) {
			for (int i = 0; i < ca.length; i++) {
				String[] tempa = t.split("");
				String[] xa = rotate(tempa, 0, i);
				String t1=Arrays.toString(xa);
				String t2=Arrays.toString(ca);
				
				if(i!=0 && (t1.equals(t2))) {
					break;
				}
				else {
					for (int j = 1; j < xa.length; j++) {
						String p1 = xa[0]+xa[j];
						if(!hm.contains(p1)) {
							hm.add(p1);
						}
					}
				}
			}
			countx++;
			
		} else {
			return hm;
		}

		//general way of writing
		while(countx<=l) {
			ArrayList<String> result = new ArrayList<>();
			String[] tempa = t.split("");
			backtrack(tempa, 0, result);
			for (String string : result) {
				String[] tempb = string.split("");
				String b="";
				String ts = stringFormer(b,tempb,countx,0);
				if(!hm.contains(ts)) {
					hm.add(ts);
				}
				
			
		}
			countx++;
		}


		return hm;
		
		

		
	}
	
	public String stringFormer(String b, String[] s, int countx, int a) {
		if(a==countx) {
			return b;
		}
		else {
			b=b+s[a];
			return stringFormer(b, s, countx, ++a);
		}
		
		
	}
	
	public ArrayList<String> backtrack(String[] s, int start, ArrayList<String> result) {
        if (start == s.length) {
        	result.add(String.join("", s));
            return result;
        }

        for (int i = start; i < s.length; i++) {
            swap(s, start, i);
            backtrack(s, start + 1, result);
            swap(s, start, i); // Backtrack
        }
        
        return result;
	}

	public void swap(String[] s, int i, int j) {
		String temp = s[i];
		s[i] = s[j];
		s[j] = temp;
	}
	
	public String[] rotate(String[] s, int a , int b) {
		
		if(a!=b) {
			String temp = s[s.length-1];
			for (int i = s.length-1; i > 0; i--) {
				s[i]=s[i-1];			
			}
			
			s[0]=temp;
			return rotate(s,++a,b);
			
		}
		else {
			return s;
		}

	}
	
	public static void main(String[] args) {
		
		comboPattern ob = new comboPattern();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the String that you want to Find all the pattern");
		String s =sc.next();
		LinkedList<String> x = ob.patternappend(s);
		System.out.println("The number of different combination that can be formed with the given string are "+x.size());
		for (String string : x) {
			System.out.println(string);
		}
	
		
	}

}
