"""
Power Of Two

Problem Statement:
Given a number N, determine whether N is a power of 2.

Input Format:
- A single line containing an integer N.

Output Format:
- Print "YES" if N is a power of 2, otherwise print "NO".

Constraints:
1 ≤ N ≤ 10^18

Example Input 1:
8

Example Output 1:
YES

Example Input 2:
10

Example Output 2:
NO

Example Input 3:
1

Example Output 3:
YES

Explanation:
- 8 (2^3) is a power of 2, so the output is "YES".
- 10 is not a power of 2, so the output is "NO".
- 1 (2^0) is a power of 2, so the output is "YES".

Approach:
- A number N is a power of 2 if it has only one bit set in its binary representation.
- We use the property: `N & (N - 1) == 0` to check if it's a power of 2.
"""

# Read an integer N from input
N = int(input())

# Check if N is a power of 2
if N > 0 and (N & (N - 1)) == 0:
    print("YES")
else:
    print("NO")
