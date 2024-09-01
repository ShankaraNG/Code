/*Q Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.*/


package practice;

class MedianSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] fin = new int[nums1.length+nums2.length];
        int n = 0;
        for (int j = 0; j < nums1.length; j++) {
          fin[n]=nums1[j];
          n=n+1;
		}
        for (int k = 0; k < nums2.length; k++) {
          fin[n]=nums2[k];
          n=n+1;
		}

        int temp;
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (fin[j] < fin[minIndex]) {
                    minIndex = j;
                }
            }
            
            if (minIndex != i) {
                temp = fin[i];
                fin[i] = fin[minIndex];
                fin[minIndex] = temp;
            }
        }
        double median;

        if(fin.length%2==0){
            median = (fin[fin.length/2-1]+fin[fin.length/2]);
            median = median/2;
        }
        else{
            median=fin[(fin.length+1)/2-1];
        }
        return median;
    }

    	public static void main(String[] args) {

		int[] num1 = {1,2};
        int[] num2 = {3,4};
        MedianSortedArrays ob = new MedianSortedArrays();
		double median = ob.findMedianSortedArrays(num1,num2);
        System.out.println(median);

	}
}
