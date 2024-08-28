/*Q Given Three arrays fidn the repeated elements in all the array
and the element repeated count should be Greated or equal to 2
Example
		int[] a = {6,39,12,22,11,16};
		int[] b = {39,46,28,22,17,14};
		int[] c = {14,22,6,9,63,72};
output
[6, 39, 14, 22]
*/

package practice;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class elements_present_in_array {
	
	public void chec(int[] a, int[] b, int[] c) {

		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

		for (int i = 0; i < a.length; i++) {
				map.put(a[i], 1);

		}
		

		
		for (int i = 0; i < b.length; i++) {
			if (map.containsKey(b[i])) {
				
				map.put(b[i], map.get(a[i])+1);
				
			}
			else {
				map.put(b[i], 1);

			}
		}
		

		
		for (int i = 0; i < c.length; i++) {
			if (map.containsKey(c[i])) {
				map.put(c[i], map.get(a[i])+1);
				
			}
			else {
				map.put(c[i], 1);

			}
		}

				
		ArrayList<Integer> cd = new ArrayList<Integer>();
			
		for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
			Integer key = entry.getKey();
			Integer val = entry.getValue();
			if (val>=2) {
				
				cd.add(key);
				
			}
		}
		System.out.println("The numbers which are repeated across the array are");
		System.out.println(cd);

	}
	
	public static void main(String[] args) {
		elements_present_in_array ob = new elements_present_in_array();
		int[] a = {6,39,12,22,11,16};
		int[] b = {39,46,28,22,17,14};
		int[] c = {14,22,6,9,63,72};
		ob.chec(a, b, c);

	}

}
