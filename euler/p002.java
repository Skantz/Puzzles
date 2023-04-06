
class p2 {
    public static void main(String[] args) {
        int a = 1;
	int b = 1;
	int sum = 0;
        while (b <= 4_000_000) {
            if (b % 2 == 0) {
	        sum += b;
	    }
	    int b_old = b;
            b = a + b;
	    a = b_old;
	}
	System.out.println(sum);
    }
}
