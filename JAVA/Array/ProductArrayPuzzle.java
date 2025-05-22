//This code is to calculate the product of a given array except the index it is on and for the number given it should give the product 
//apart from that number


package practice;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.Scanner;

public class ProductArrayPuzzle {
	
	
	public HashMap<String, Object> productmethod1(int[] a, int num) {
		int[] productarray = new int[a.length];
		int index = -1;
		
		for (int i = 0; i < a.length; i++) {
			int product = 1;
			for (int j = 0; j < a.length; j++) {
				if(i!=j)
				{
					product = product*a[j];
					if(a[j]==num) {
						index = j;
					}
				}
				productarray[i] = product;
				
			}
			
		}
		int productforthatnumber = productarray[index];
		HashMap<String, Object> productnumber = new HashMap<String, Object>();
		productnumber.put("Array", productarray);
		productnumber.put("Number", productforthatnumber);	
		return productnumber;	

	}
	
	public HashMap<String, Object> productmethod2(int[] a, int num) {
		int[] productarray = new int[a.length];
		int index = -1;
		
		for (int i = 0; i < a.length; i++) {
			int product = 1;
			for (int j = 0; j < a.length; j++) {
				if(i!=j)
				{
					product = product*a[j];
					if(a[j]==num) {
						index = j;
					}
				}
				productarray[i] = product;
				
			}
			
		}
		int product = 1;
		for (int i = 0; i < a.length; i++) {
			product = product*a[i];
		}
		
		int productforthatnumber = product/num;
		HashMap<String, Object> productnumber = new HashMap<String, Object>();
		productnumber.put("Array", productarray);
		productnumber.put("Number", productforthatnumber);	
		return productnumber;	

	}

	public HashMap<String, Object> productmethod3(int[] a, int num) {
	    int index = -1;
	    for (int i = 0; i < a.length; i++) {
	        if (a[i] == num) {
	            index = i;
	            break;
	        }
	    }

	    int[] leftarray = new int[a.length];
	    int[] rightarray = new int[a.length];

	    leftarray[0] = 1;
	    for (int i = 1; i < a.length; i++) {
	        leftarray[i] = leftarray[i - 1] * a[i - 1];
	    }

	    rightarray[a.length - 1] = 1;
	    for (int i = a.length - 2; i >= 0; i--) {
	        rightarray[i] = rightarray[i + 1] * a[i + 1];
	    }

	    int[] finalarray = new int[a.length];
	    for (int i = 0; i < a.length; i++) {
	        finalarray[i] = leftarray[i] * rightarray[i];
	    }

	    int productforthatnumber = finalarray[index];

	    HashMap<String, Object> productnumber = new HashMap<>();
	    productnumber.put("Array", finalarray);
	    productnumber.put("Number", productforthatnumber);
	    return productnumber;
	}
	
	public static void main(String[] args) {
		ProductArrayPuzzle obj = new ProductArrayPuzzle();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the Size of the Array you want");
		int size = sc.nextInt();
		int [] a = new int[size];
		System.out.println("Enter the Elements to calculate the product array");
		for (int i = 0; i < size; i++) {
			a[i] = sc.nextInt();			
		}
		System.out.println("Enter the Number in the Array you want to Skip");
		int num = sc.nextInt();
		System.out.println("The given array is as mentioned below");
		System.out.println(Arrays.toString(a));
		System.out.println("Enter the Option to calculate the Product Array");
		System.out.println("1: Calculate product by Skipping that number\n2: Calculate by Division method\n3: Calculate the product of array skipping the number from left and right");
		int option = sc.nextInt();
		HashMap< String, Object> result = new HashMap<String, Object>();
		switch (option) {
	    case 1:
	    	result = obj.productmethod1(a, num);
	        break;
	    case 2:
	    	result = obj.productmethod2(a, num);
	        break;
	    case 3:
	    	result = obj.productmethod3(a, num);
	        break;
	    default:
	        System.out.println("Invalid Input selected.");
	}
		for (Entry<String, Object> entry : result.entrySet()) {
			String key = entry.getKey();
			Object val = entry.getValue();
			if(key == "Array") {
				System.out.println("The Result Product Array is " + Arrays.toString((int[]) val));
			}
			if(key == "Number") {
				System.out.println("The Result Product of the Array except for the number " + num + " is " + val.toString());
			}
		}
		
		
	}

}
