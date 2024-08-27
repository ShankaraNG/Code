/*Given a number to convert it into Readable format
example
1245612
One Million Two Hundred Fourty Five Thousand Six Hundred Twelve */



package practice;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map.Entry;
import java.util.Scanner;

public class number_to_words {

	public void length(long num) {
		long count=0;
		long temp;
		ArrayList<Long> h = new ArrayList<Long>();
		ArrayList<Long> t = new ArrayList<Long>();
		ArrayList<Long> m = new ArrayList<Long>();
		ArrayList<Long> b = new ArrayList<Long>();
		ArrayList<Long> tr = new ArrayList<Long>();
		for (long i = num; i > 0; i=i/1000) {
			temp=i%1000;
			if (count==0) {
				for (long j = temp; j > 0; j=j/10) {
					h.add(j%10);		
				}
				count++;
				Collections.reverse(h);
			}
			else if(count==1){
				for (long j = temp; j > 0; j=j/10) {
					t.add(j%10);		
				}
				count++;
				Collections.reverse(t);
			}
			else if(count==2){
				for (long j = temp; j > 0; j=j/10) {
					m.add(j%10);		
				}
				count++;
				Collections.reverse(m);
			}
			else if(count==3)
			{
				for (long j = temp; j > 0; j=j/10) {
					b.add(j%10);		
				}
				count++;
				Collections.reverse(b);
			}
			else if(count==4)
			{
				for (long j = temp; j > 0; j=j/10) {
					tr.add(j%10);		
				}
				count++;
				Collections.reverse(tr);
			}
			else {
				break;
			}
		}

		StringBuffer hun = new StringBuffer();
		
		if (!tr.isEmpty()) {
			Iterator<Long> e =tr.iterator();
			long count1;
			long position;
			if (tr.size()==1) {
				count1 =3;
				position =3;
			}
			else if (tr.size()==2){
				count1 =2;
				position =2;
			}
			else {
				count1 =1;
				position =1;
			}
			while (e.hasNext()) {
				long integer = (long) e.next();
				if (integer==0) {
					position++;
					count1++;
					continue;
				}
				else if (integer==1 && count1==2) {
					count1++;
					continue;
				}
				else {
					String s = callingnum(integer, position, count1);
					hun.append(s);
					position++;
					count1++;
				}
				
			}
			
			hun.append("Trillion ");

		}
		
		if (!b.isEmpty()) {
			Iterator<Long> e =b.iterator();
			long count1;
			long position;
			if (b.size()==1) {
				count1 =3;
				position =3;
			}
			else if (b.size()==2){
				count1 =2;
				position =2;
			}
			else {
				count1 =1;
				position =1;
			}
			while (e.hasNext()) {
				long integer = (long) e.next();
				if (integer==0) {
					position++;
					count1++;
					continue;
				}
				else if (integer==1 && count1==2) {
					count1++;
					continue;
				}
				else {
					String s = callingnum(integer, position, count1);
					hun.append(s);
					position++;
					count1++;
				}
				
			}
			
			hun.append("Billion ");

		}
		
		if (!m.isEmpty()) {
			Iterator<Long> e =m.iterator();
			long count1;
			long position;
			if (m.size()==1) {
				count1 =3;
				position =3;
			}
			else if (m.size()==2){
				count1 =2;
				position =2;
			}
			else {
				count1 =1;
				position =1;
			}
			while (e.hasNext()) {
				long integer = (long) e.next();
				if (integer==0) {
					position++;
					count1++;
					continue;
				}
				else if (integer==1 && count1==2) {
					count1++;
					continue;
				}
				else {
					String s = callingnum(integer, position, count1);
					hun.append(s);
					position++;
					count1++;
				}
				
			}
			
			hun.append("Million ");

		}
		
		if (!t.isEmpty()) {
			Iterator<Long> e =t.iterator();
			long count1;
			long position;
			if (t.size()==1) {
				count1 =3;
				position =3;
			}
			else if (t.size()==2){
				count1 =2;
				position =2;
			}
			else {
				count1 =1;
				position =1;
			}
			while (e.hasNext()) {
				long integer = (long) e.next();
				if (integer==0) {
					position++;
					count1++;
					continue;
				}
				else if (integer==1 && count1==2) {
					count1++;
					continue;
				}
				else {
					String s = callingnum(integer, position, count1);
					hun.append(s);
					position++;
					count1++;
				}
				
			}
			
			hun.append("Thousand ");

		}
		
		if (!h.isEmpty()) {
			Iterator<Long> e =h.iterator();
			long count1;
			long position;
			if (h.size()==1) {
				count1 =3;
				position =3;
			}
			else if (h.size()==2){
				count1 =2;
				position =2;
			}
			else {
				count1 =1;
				position =1;
			}
			
			while (e.hasNext()) {
				long integer = (long) e.next();
				if (integer==0) {
					position++;
					count1++;
					continue;
				}
				else if (integer==1 && count1==2) {
					count1++;
					continue;
				}
				else {
					String s = callingnum(integer, position, count1);
					hun.append(s);
					position++;
					count1++;
				}
				
			}

		}
		
		System.out.println(hun.toString());

	}

	public String callingnum(long num,long count, long position) {
		HashMap<Long, String> s = new HashMap<Long, String>();
		HashMap<Long, String> t = new HashMap<Long, String>();
		HashMap<Long, String> tw = new HashMap<Long, String>();
		s.put((long) 1, "One");
		s.put((long) 2, "Two");
		s.put((long) 3, "Three");
		s.put((long) 4, "Four");
		s.put((long) 5, "Five");
		s.put((long) 6, "Six");
		s.put((long) 7, "Seven");
		s.put((long) 8, "Eight");
		s.put((long) 9, "Nine");
		t.put((long) 2, "Twenty");
		t.put((long) 3, "Thirty");
		t.put((long) 4, "Fourty");
		t.put((long) 5, "Fifty");
		t.put((long) 6, "Sixty");
		t.put((long) 7, "Seventy");
		t.put((long) 8, "Eighty");
		t.put((long) 9, "Ninty");
		tw.put((long) 1, "Eleven");
		tw.put((long) 2, "Twelve");
		tw.put((long) 3, "Thirteen");
		tw.put((long) 4, "Fourteen");
		tw.put((long) 5, "Fifteen");
		tw.put((long) 6, "Sixteen");
		tw.put((long) 7, "Seventeen");
		tw.put((long) 8, "Eighteen");
		tw.put((long) 9, "Nineteen");
		String r =null;
		if ((count==1 && count==position)|| (count==3 && count==position)) {
			for (Entry<Long, String> entry : s.entrySet()) {
				Long key = entry.getKey();
				if (num==key && count==1) {
					r = entry.getValue() + " Hundred" + " ";
					break;
				}
				else if(num==key && count==3) {
					r = entry.getValue() + " ";
					break;
				}
				else {
					continue;
				}
			}
		}
		else if (count==2 && count==position) {

			for (Entry<Long, String> entry : t.entrySet()) {
				Long key = entry.getKey();
				if (num==key && count==2) {
					r = entry.getValue() + " ";
					break;
				}

			}
		}
		else {
			for (Entry<Long, String> entry : tw.entrySet()) {
				Long key = entry.getKey();
				if (num==key && count==2) {
					r = entry.getValue() + " ";
					break;
				}

			}
		}
		
		return r;
	}
	
	public static void main(String[] args) {
		number_to_words obj = new number_to_words();
		System.out.println("Enter the number");
		try (Scanner a = new Scanner(System.in)) {
			long num = a.nextLong();
			obj.length(num);
		}
	}
	

}
