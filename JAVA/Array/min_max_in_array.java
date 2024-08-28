package practice;

public class min_max_in_array {
	
	public int min(int[] a) {
		int less = a[0];
		for (int i = 0; i < a.length-1; i++) {
			if (a[i]<less) {
				less = a[i];
			}
		}
		
		return less;

	}
	
	public int max(int[] a) {
		int max = a[0];
		for (int i = 0; i < a.length-1; i++) {
			if (a[i]>max) {
				max = a[i];
			}
		}
		
		return max;

	}
	
	public static void main(String[] args) {
		
		int[] ob = {10,40,30,100,20,40};
		min_max_in_array bo = new min_max_in_array();
		int a = bo.max(ob);
		System.out.println(a);
		int b = bo.min(ob);
		System.out.println(b);
		
	}

}
