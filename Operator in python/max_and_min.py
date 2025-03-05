"""
Max and Min

Problem Statement:
Given three numbers A, B, and C, determine and print the minimum and maximum numbers.

Input Format:
- A single line containing three space-separated integers A, B, and C.

Output Format:
- Print the minimum number followed by a single space and then the maximum number.

Constraints:
-10^5 ≤ A, B, C ≤ 10^5

Example Input 1:
1 2 3

Example Output 1:
1 3

Example Input 2:
10 20 -5

Example Output 2:
-5 20

Example Input 3:
-1 -2 -3

Example Output 3:
-3 -1

Explanation:
- In the first case, the minimum value is 1, and the maximum is 3, so the output is "1 3".
- In the second case, the minimum value is -5, and the maximum is 20, so the output is "-5 20".
- In the third case, the minimum value is -3, and the maximum is -1, so the output is "-3 -1".
"""

# Read three integers from input
a, b, c = map(int, input().split())

# Print the minimum and maximum values
print(min(a, b, c), max(a, b, c))
