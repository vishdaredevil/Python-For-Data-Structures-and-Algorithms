"""
The Brothers

Problem Statement:
You are given the names of two persons. Each person has a first name and a second name.
Two persons are considered brothers if they share the same second name.

Input Format:
- First line contains two strings F1, S1 (first and second name of the first person).
- Second line contains two strings F2, S2 (first and second name of the second person).

Output Format:
- Print "ARE Brothers" if they have the same second name, otherwise print "NOT".

Constraints:
1 ≤ |F1|, |S1|, |F2|, |S2| ≤ 10⁵
(All names are in lowercase English letters.)

Example Input 1:
narendra modi
giorgia meloni

Example Output 1:
NOT

Example Input 2:
sunny leone
sunny deol

Example Output 2:
NOT

Example Input 3:
salman khan
amir khan

Example Output 3:
ARE Brothers

Explanation:
- In the first case, "modi" ≠ "meloni", so the output is "NOT".
- In the second case, "leone" ≠ "deol", so the output is "NOT".
- In the third case, "khan" = "khan", so the output is "ARE Brothers".
"""

# Read the first and second names of both persons
f1, s1 = input().split()
f2, s2 = input().split()

# Check if they share the same second name
if s1 == s2:
    print("ARE Brothers")
else:
    print("NOT")
