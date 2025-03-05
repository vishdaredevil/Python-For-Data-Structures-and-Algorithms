# Mathematical Expression

# Description:
# Given a mathematical expression. The expression will be one of the following expressions:
# A + B = C, A - B = C, and A * B = C
#
# where A, B, C are three numbers, S is the sign between A and B, and Q is the equals sign '='.
#
# Print "Yes" if the expression is Right, otherwise print the right answer of the expression.
#
# Input Format:
# Only one line containing the expression: A, S, B, Q, C respectively.
# S can be ('+', '-', '*', '/') without the quotation marks.
# Note: Division sign ('/') means integer division operator.
#
# Output Format:
# Output a single line representing the answer to the query.
#
# Constraints:
# 0 ≤ A, B ≤ 100
# -10^5 ≤ C ≤ 10^5
#
# Sample Input 1:
# 5 + 10 = 15
# Sample Output 1:
# Yes
#
# Sample Input 2:
# 2 * 10 = 19
# Sample Output 2:
# 20
#
# Sample Input 3:
# 3 - 1 = 2
# Sample Output 3:
# Yes

# Read input
a, s, b, q, c = input().split()  
a, b, c = int(a), int(b), int(c)  

# Perform the operation
if s == '+':  
    ans = a + b  
elif s == '-':  
    ans = a - b  
elif s == '*':  
    ans = a * b  
elif s == '/':  
    ans = a // b  

# Print the result
if ans == c:  
    print("Yes")  
else:  
    print(ans)
