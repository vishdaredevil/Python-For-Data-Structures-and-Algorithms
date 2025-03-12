"""greatest common divisor  

problem statement:  
given two numbers a and b, print their greatest common divisor (gcd).  

note: the gcd of two or more integers, which are not all zeroes, is the largest positive integer that divides each of the integers.  

input format:  
- only one line containing two integers a and b.  

output format:  
print the gcd of a and b.  

constraints:  
- 1 ≤ a, b ≤ 10³  

sample input 1  
12 8  

sample output 1  
4  

sample input 2  
3 7  

sample output 2  
1  

sample input 3  
5 10  

sample output 3  
5  """
# Write your code here
a,b=map(int,input().split())
c=[]
for i in range(1,b+1):
    if a%i==0 and b%i==0:
        c.append(i)
print (max(c))