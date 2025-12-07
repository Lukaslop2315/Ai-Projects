import java.util.Scanner; 

// AI search algorithm for DFS with backtracking (inefficient but is easy to understand and visualize)  made by Lukas.L coded in JAVA must use Java IDE to use.

public class QueenProblem {
	
	static int solutionsFound = 0;              // 2 global variables :counter for how many solutions found
	private static boolean solutionPrinted = false;       // to make sure the first solution is printed 
	
	public static void main(String[] args)
	{
		
		Scanner input = new Scanner(System.in);
		System.out.print("Enter 'N' board Shape, where the board is N x N size");   // input N
		int Nsize = input.nextInt();
		boardNxN(Nsize);
		System.out.println();
		System.out.println("Amount of solutions found: "+ solutionsFound);
		input.close();
		
		
		
	}
	
	public static void boardNxN(int Nsize) {
		System.out.print("Creating board size "+ Nsize +"x" + Nsize + "....");
		char[][] boardShape = new char[Nsize][Nsize]; //char[][] boardShape is 2d array of size N×N will use in every function so it is important.
		for (int row = 0; row < Nsize; row++) {                // goes through every single square
			for(int col = 0; col < Nsize; col++) { 
				boardShape[row][col] = '.';            // shapes the 2d array and adds a empty board to each square '.' represent empty square 
		
			}
			
		    
		}
		long start = System.currentTimeMillis();  //start the timer
		placeQueens(boardShape,0, Nsize); // PRINT OUT THE FIRST SOLUTION possible starting with row[0] so all the squares are checked
	    long end = System.currentTimeMillis();//  end the timer
	    long totalTimeInMs = end - start; 
		float convertedSeconds =  totalTimeInMs / 1000.0f ;  //convert milliseconds into seconds
		System.out.print("time taken " + convertedSeconds+" seconds");
	}
	
	public static boolean safePosition(char[][] boardShape, int row , int col , int Nsize) {  //boolean function to return true/false for if statements safe or not
		// check the rest of the row
	   // removed Lower Diagonal checks because impossible to have Queens below when first checking
		for (int i = 0; i < row; i++){                               // row
	       if (boardShape[i][col] == 'X') { // 'X' represent queen
	    	    return false;
	       }
	}
		for (int r = row-1, c = col-1; r>=0 && c>=0; r--, c--) {       // upper left diagonal check
	        if (boardShape[r][c] == 'X') {
	            return false;
	        }
	    }
		for (int r = row-1, c = col+1; r >= 0 && c < Nsize; r--, c++) {       // upper right diagonal row -1 col+1   row goes up down/ col left right
	        if (boardShape[r][c] == 'X') {
	            return false;
	        }
	    }
		//for (int i = 0; i < Nsize; i++){                               //  column check
		      // if (boardShape[row][i] == 'X') {
		    	   // return false;
		       //}
		//}
		

		//for (int r = row+1, c = col+1; r < Nsize && c <Nsize; r++, c++) {       // lower right diagonal  
	       // if (boardShape[r][c] == 'X') {
	          //  return false;
	       // }
	   // }
		//for (int r = row+1, c = col-1; r < Nsize && c>=0; r++, c--) {       // lower left diagonal  row +1 col-1   row goes up down/ col left right
	       // if (boardShape[r][c] == 'X') {
	           // return false;
	       // }
	   // }
		
		return true;
}
	public static void placeQueens(char[][] boardShape, int row, int Nsize) {   //place the actual queens in the correct space and check possible solutions
	    if (row == Nsize) { // when finished                                                
	    	solutionsFound++;
	    	
	    	if (solutionPrinted == false) {
	    		System.out.println();
                System.out.println("First solution:");
                printBoard(boardShape, Nsize);
                solutionPrinted = true;
	    	 
            }
	    	          return;       
	    	                                                             // recursive checking is O(n!) for the solution checking 
	    }                                                             
	    for (int c = 0; c < Nsize; c++) {                              // go through each column in the row
            if (safePosition(boardShape, row, c,Nsize))  {    // if this is true (does not attack a queen can be placed
            	boardShape[row][c] = 'X';                                 // place Queen in the place 'X' represent queen
                placeQueens(boardShape, row + 1, Nsize);                //re check all columns in the next row if any are viable
                boardShape[row][c] = '.';                   // remove all the marks to check more solutions because if you keep the queens position then other solutions are not viable
            }
	      
        }
	    
	}
	public static void printBoard(char[][]boardShape, int Nsize) {
		for (int row = 0; row < Nsize; row++) {                     // iterate through and print each square in the 2d Array
	        for (int col = 0; col < Nsize; col++) {
	            System.out.print(boardShape[row][col] + "  "); 
	        }
	        System.out.println();  // new line
	    }
	}
}
