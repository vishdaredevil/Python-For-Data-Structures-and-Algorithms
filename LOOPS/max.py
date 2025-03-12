"""find the maximum number  

problem statement:  
given a number n and n numbers, find the maximum number among these n numbers.  

input format:  
- the first line contains an integer n.  
- the second line contains n integers xᵢ, where 1 ≤ i ≤ n.  

output format:  
print the maximum number.  

constraints:  
- 1 ≤ n ≤ 10³  
- 0 ≤ xᵢ ≤ 10⁹  

sample input 1  
5  
1 8 5 7 5  

sample output 1  
8  

sample input 2  
2  
2 2  

sample output 2  
2  """
# Write your code here
n=int(input())
n1=list(map(int,input().split()))
print (max(n1))