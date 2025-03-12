# Even Numbers  

# Problem Statement:  
# Given a number N, print all even numbers between 1 and N (inclusive), each on a separate line. If there are no even numbers, print -1.  

# Input Format:  
# - A single integer N.  

# Output Format:  
# - Print all even numbers from 1 to N, each on a new line.  
# - If no even numbers exist in the range, print -1.  

# Constraints:  
# - 1 ≤ N ≤ 10³  

# Sample Input 1  
# 10  

# Sample Output 1  
# 2  
# 4  
# 6  
# 8  
# 10  

# Sample Input 2  
# 5  

# Sample Output 2  
# 2  
# 4
n=int(input())
if n==1:
    print (-1)
else:
    for i in range(1,n+1):
        if i%2==0:
            print (i)
        