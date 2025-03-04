"""
Simple Calculator

Problem Statement:
Given two numbers X and Y, print their summation, multiplication, and subtraction.

Input Format:
A single line containing two integers X and Y separated by a space.

Output Format:
Print three lines in the following format:
1. X + Y = (summation result)
2. X * Y = (multiplication result)
3. X - Y = (subtraction result)

Constraints:
1 ≤ X, Y ≤ 10^5

Example Input 1:
5 10

Example Output 1:
5 + 10 = 15
5 * 10 = 50
5 - 10 = -5

Example Input 2:
12345 54321

Example Output 2:
12345 + 54321 = 66666
12345 * 54321 = 670592745
12345 - 54321 = -41976
"""

# Read input values
x, y = map(int, input().split())

# Perform calculations and print results
print(x, "+", y, "=", x + y)
print(x, "*", y, "=", x * y)
print(x, "-", y, "=", x - y)