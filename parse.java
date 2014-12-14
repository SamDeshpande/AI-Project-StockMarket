import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;


public class parse {
	final static int n_files = 8;

	public static void main(String[] args) throws IOException  {
		// TODO Auto-generated method stub
		
		Scanner scan_bse = new Scanner(new File("bseJan2005Dec2014.csv"));
		Scanner scan_dax = new Scanner(new File("daxJan2005Dec2014.csv"));
		Scanner scan_hkex = new Scanner(new File("hkexJan2005Dec2014.csv"));
		Scanner scan_lse = new Scanner(new File("lseJan2005Dec2014.csv"));
		Scanner scan_nasdaq = new Scanner(new File("nasdaqJan2005Dec2014.csv"));
		Scanner scan_nikkei = new Scanner(new File("nikkeiJan2005Dec2014.csv"));
		Scanner scan_nse = new Scanner(new File("nseJan2005Dec2014.csv"));
		Scanner scan_hang = new Scanner(new File("hangshengJan2005Dec2014.csv"));
		
		
		
		scan_bse.nextLine();
		scan_dax.nextLine();
		scan_hkex.nextLine();
		scan_lse.nextLine();
		scan_nasdaq.nextLine();
		scan_nikkei.nextLine();
		scan_nse.nextLine();
		scan_hang.nextLine();
		
		Scanner[] arr = new Scanner[n_files];
		
		arr[0] = scan_bse;
		arr[1] = scan_dax;
		arr[2] = scan_hkex;
		arr[3] = scan_lse;
		arr[4] = scan_nasdaq;
		arr[5] = scan_nikkei;
		arr[6] = scan_nse;
		arr[7] = scan_hang;
		
		int zero_counter = 0;
		
		String[][] parts = new String[n_files][];
		PrintWriter[] results = new PrintWriter[n_files];
		
		for(int i =0 ; i < n_files; i++) {
			results[i] = new PrintWriter( i+ ".txt");
		}
		
		
		while(scan_bse.hasNext() && scan_dax.hasNext() && scan_hkex.hasNext()
				&& scan_lse.hasNext() && scan_nasdaq.hasNext() && scan_nikkei.hasNext()
				&& scan_nse.hasNext() && scan_hang.hasNext()) {
			boolean flag = false;
			
			for(int i =0; i < n_files; i++) {
				String str = arr[i].nextLine();
				parts[i] = str.split(",");
			}
			
			for(int i= 1 ; i < n_files; i++) {
				if(!parts[i][0].equals(parts[0][0])) {
			//		flag = true;
				}
			}
			
			if(flag) {
				break;
			}
			
			for(int i =0; i < n_files; i++) {
				String date = parts[i][0];
				Double start = Double.parseDouble(parts[i][1]);
				Double close = Double.parseDouble(parts[i][4]);
				double change = close - start;
				if(change == 0) {
					zero_counter++;
				}
				change = change;
				results[i].println(date);
				results[i].println(change);
			}
			
		}
		for(int i =0; i < n_files; i++) {
			results[i].close();
		}
		for(int i =0; i < n_files; i++) {
			arr[i].close();
		}
		
		System.out.println(zero_counter + " " + zero_counter);

	}

}
