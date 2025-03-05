"""
Capital or Small or Digit

Problem Statement:
Given a character X, determine whether it is a digit or an alphabet.
If it is an alphabet, determine whether it is a capital letter or a small letter.

Input Format:
- A single character X, which can be a digit ('0'-'9'), an uppercase letter ('A'-'Z'), or a lowercase letter ('a'-'z').

Output Format:
- If X is a digit, print "IS DIGIT".
- If X is an alphabet, print "ALPHA" on the first line.
  - If it is uppercase, print "IS CAPITAL".
  - If it is lowercase, print "IS SMALL".

Constraints:
- The character X will always be from the given range.

Example Input 1:
A

Example Output 1:
ALPHA
IS CAPITAL

Example Input 2:
a

Example Output 2:
ALPHA
IS SMALL

Example Input 3:
9

Example Output 3:
IS DIGIT

Explanation:
- 'A' is an uppercase letter, so output "ALPHA" followed by "IS CAPITAL".
- 'a' is a lowercase letter, so output "ALPHA" followed by "IS SMALL".
- '9' is a digit, so output "IS DIGIT".
"""

# Read input character
x = input()

# Check if it's a digit
if x.isdigit():
    print("IS DIGIT")
# Check if it's an alphabet
elif x.isalpha():
    print("ALPHA")
    if x.isupper():
        print("IS CAPITAL")
    else:
        print("IS SMALL")