/*Q Longest Palindromic Substring
Solved
Medium
Topics
Companies
Hint
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
*/

package practice;


public class longest_palindrome {
	
	public String longestPalindrome(String s) {
		StringBuilder a = new StringBuilder();
		StringBuilder b = new StringBuilder();
		char[] arr = s.toCharArray();
		String pal=String.valueOf(arr[0]);
		int max =0;
		for (int i = 0; i < arr.length-1; i++) {
			a.setLength(0);
			a.append(arr[i]);
			for (int j = i+1; j < arr.length; j++) {
				b.setLength(0);
				a.append(arr[j]);
				String sa = a.toString();
				String as = a.reverse().toString();
				
				if (sa.equals(as)&&a.length()>max) {
					max=a.length();
					pal=a.toString();
				}
				a.reverse();
			}
		}
		return pal;
	}
	
	public static void main(String[] args) {
		longest_palindrome obj = new longest_palindrome();
		String S ="abc";
		System.out.println(obj.longestPalindrome(S));
	}

}
