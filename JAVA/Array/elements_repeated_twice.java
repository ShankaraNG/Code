/*Given an array find the elements which are repeated twice. */

package practice;

import java.util.HashMap;
import java.util.Map;

public class array_count_check1 {

	private void chec(int[] a) {

		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

		for (int i = 0; i < a.length; i++) {
			int count = 0;
			for (int j = 0; j < a.length; j++) {

				if (a[i]==a[j]) {
					count++;
				}

			}
			//System.out.println("The element " + a[i] + " has a count of " + count);
			map.put(a[i], count);

		}
		
		for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
			Integer key = entry.getKey();
			Integer val = entry.getValue();
			if(val==2) {
			System.out.println(key+ "=" + val);
			}
		}

	}

	public static void main(String[] args) {

		int[] b = {10,20,10,30,40};
		array_count_check1 c = new array_count_check1();
		c.chec(b);
	}

}
