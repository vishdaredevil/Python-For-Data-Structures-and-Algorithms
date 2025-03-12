"""find all divisors  

problem statement:  
given a number n, print all its divisors in ascending order.  

input format:  
- only one line containing an integer n.  

output format:  
print all positive divisors of n, one number per line.  

constraints:  
- 1 ≤ n ≤ 10⁴  

sample input 1  
6  

sample output 1  
1  
2  
3  
6  

sample input 2  
4  

sample output 2  
1  
2  
4  

sample input 3  
7  

sample output 3  
1  
7  """
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print (i)