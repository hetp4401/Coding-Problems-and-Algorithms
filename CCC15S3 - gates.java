package dataStructures;

import java.util.ArrayList;
import java.util.Scanner;

public class ccc15s3 {

    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        int g = s.nextInt();
        int pp = s.nextInt();
        int success = 0;

        plane[] gates = new plane[g + 2];

        for (int i = 0; i < pp; i++) {

            int index = s.nextInt();
            plane p = new plane();
            ArrayList<plane> li = new ArrayList();

            while (gates[index] != null) {
                li.add(gates[index].parent);
                index = gates[index].parent.val;
                if (index == 0) {
                    System.out.println(success);
                    System.exit(0);
                }
            }

            if (gates[index + 1] == null) {
                plane parent = new plane();
                parent.val = index - 1;
                p.parent = parent;
            } else if (gates[index + 1] != null) {
                plane parent = gates[index + 1].parent;
                parent.val = index - 1;
                p.parent = parent;
            }

            for (plane pl : li) {
                pl.val = index - 1;
            }
            gates[index] = p;
            success++;
            li.clear();
        }
        System.out.println(success);
    }
}

class plane {

    plane parent;
    int val;

    plane() {
    }
}


/*
For your birthday, you were given an airport.

The airport has G gates, numbered from 1 to G.

P planes arrive at the airport, one after another. You are to assign the i-th plane to permanently dock at any gate 1, …, gi (1 ≤ gi ≤ G), at which no previous plane has docked. As soon as a plane cannot dock at any gate, the airport is shut down and no future planes are allowed to arrive.

In order to keep the person who gave you the airport happy, you would like to maximize the number of planes starting from the beginning that can all dock at different gates.

Input
The first line of input contains G (1 ≤ G ≤ 105), the number of gates at the airport.
The second line of input contains P (1 ≤ P ≤ 105), the number of planes which will land.
The next P lines contain one integer gi (1 ≤ gi ≤ G), such that the ith plane must dock at some gate from 1 to gi, inclusive.

Note that for at least 40% of the marks for this question, P ≤ 2000 and G ≤ 2000.

Output
Output the maximum number of planes that can land starting from the beginning.

Sample Input 1
4
3
4
1
1

Sample Output 1
2

Explanation of Sample 1
The first plane can go anywhere, but it is best to not put it into Gate 1. Notice that planes 2 and 3 both want to dock into Gate 1, so plane 3 is unable to dock.

Sample Input 2
4
6
2
2
3
3
4
4

Sample Output 2
3

Explanation of Sample 2
The first two planes will dock in gates 1 and 2 (in any order). The third plane must dock at Gate 3. Thus, the fourth plane cannot dock anywhere, and the airport is closed, even though plane 5 would have been able to dock.

*/