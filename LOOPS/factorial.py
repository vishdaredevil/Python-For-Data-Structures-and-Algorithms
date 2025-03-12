"""find the factorial  

problem statement:  
given a number n, print the factorial of n.  

input format:  
- the first line contains an integer t, the number of test cases.  
- the next t lines each contain an integer n.  

output format:  
for each test case, print a single line containing the factorial of n.  

constraints:  
- 1 ≤ t ≤ 15  
- 0 ≤ n ≤ 20  

sample input 1  
2  
5  
3  

sample output 1  
120  
6  """
# Write your code here
t=int(input())
for j in range(t):
    n=int(input())
    f=1
    for i in range(1,n+1):
        f=f*i
    print (f)

