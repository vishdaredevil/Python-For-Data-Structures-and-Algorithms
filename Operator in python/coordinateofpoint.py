"""
Coordinates of a Point

Problem Statement:
Given the coordinates (X, Y) of a point in a 2D plane, determine its location:
- If the point is at the origin (0,0), print "Origem".
- If the point is on the X-axis (Y=0 and X≠0), print "Eixo X".
- If the point is on the Y-axis (X=0 and Y≠0), print "Eixo Y".
- Otherwise, print Q1, Q2, Q3, or Q4 based on the quadrant.

Quadrants:
- Q1: X > 0 and Y > 0
- Q2: X < 0 and Y > 0
- Q3: X < 0 and Y < 0
- Q4: X > 0 and Y < 0

Input Format:
- The first line contains an integer T, the number of test cases.
- Each test case consists of two space-separated floating-point numbers X and Y.

Output Format:
- For each test case, print the appropriate output on a new line.

Constraints:
1 ≤ T ≤ 10^6
-1000 ≤ X, Y ≤ 1000

Example Input 1:
1
4.5 -2.2

Example Output 1:
Q4

Example Input 2:
1
0.1 0.1

Example Output 2:
Q1

Explanation:
- (4.5, -2.2) is in Q4 as X > 0 and Y < 0.
- (0.1, 0.1) is in Q1 as X > 0 and Y > 0.
"""

# Read number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    x, y = map(float, input().split())

    if x == 0 and y == 0:
        print("Origem")
    elif x == 0:
        print("Eixo Y")
    elif y == 0:
        print("Eixo X")
    elif x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y > 0:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    else:
        print("Q4")
