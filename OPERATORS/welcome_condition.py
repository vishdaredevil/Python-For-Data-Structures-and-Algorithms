"""
Welcome Conditions

Problem Statement:
Given T test cases, each containing two integers A and B, print "Yes" if A is greater than or equal to B, otherwise print "No".

Input Format:
- The first line contains an integer T, the number of test cases.
- Each of the next T lines contains two space-separated integers A and B.

Output Format:
- Print "Yes" if A ≥ B, otherwise print "No".

Constraints:
1 ≤ T ≤ 10
1 ≤ A, B ≤ 100

Example Input 1:
1
10 9

Example Output 1:
Yes

Example Input 2:
1
5 7

Example Output 2:
No

Example Input 3:
1
5 5

Example Output 3:
Yes

Explanation:
- In the first case, A = 10 and B = 9. Since A ≥ B, the output is "Yes".
- In the second case, A = 5 and B = 7. Since A is not ≥ B, the output is "No".
- In the third case, A = 5 and B = 5. Since A ≥ B, the output is "Yes".
"""

# Read the number of test cases
t = int(input())

# Loop through each test case
for _ in range(t):
    a, b = map(int, input().split())  # Read two integers
    if a >= b:
        print("Yes")
    else:
        print("No")