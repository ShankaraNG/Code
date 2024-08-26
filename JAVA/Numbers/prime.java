package practice;

public class prime {

	int startnum;
	int endnum;

	public prime(int startnum, int endnum) {
		this.startnum = startnum;
		this.endnum=endnum;
	}

	public int primeprint() {
		int count = 0;
		if (startnum ==1) {
			startnum++;

		}
		if (startnum ==0) {
			startnum+=2;
		}
		for (int i = startnum; i <= endnum; i++) {

			boolean flag = true;
			for (int j=2 ; j <=i/2; j++) {

				if (i%j==0)
				{
					flag = false;
					break;
				}

			}

			if (flag) {
				System.out.println(i);
				count++;
			}

		}
		return count;
	}

	public static void main(String[] args) {

		prime ob = new prime(1, 1000);
		int count = ob.primeprint();
		System.out.println("The total count of number is " + count);
	}

}
