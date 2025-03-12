"""problem statement:
given n numbers, count how many of them are even, odd, positive, and negative.

input format:

the first line contains an integer n, representing the number of values.
the second line contains n integers, where the i-th number from the start is called xᵢ.
output format:
print four lines with the following format:

first line: "even: x", where x is the count of even numbers.
second line: "odd: x", where x is the count of odd numbers.
third line: "positive: x", where x is the count of positive numbers.
fourth line: "negative: x", where x is the count of negative numbers.
constraints:

1 ≤ n ≤ 10³
-10⁵ ≤ xᵢ ≤ 10⁵
sample input 1
5
-5 0 -3 -4 12

sample output 1
even: 3
odd: 2
positive: 1
negative: 3"""
# Write your code here
n=int(input())
e,o,p,n,z=0,0,0,0,0
n1=list(map(int,input().split()))
for i in n1:
    if i%2==0:
        e=e+1
        
    if i%2!=0:
        o=o+1
        
    if i>0:
        p=p+1
        
    if i<0:
        n=n+1
        
print ("Even:",e) 
print ("Odd:",o)
print ("Positive:",p)
print ("Negative:",n)
