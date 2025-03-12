"""lucky numbers  

problem statement:  
given two numbers a and b, print all lucky numbers between a and b inclusive.  

note:  
a lucky number is any positive number whose decimal representation contains only the digits 4 and 7.  

for example: numbers 4, 7, 47, and 744 are lucky, whereas numbers 5, 17, and 174 are not.  

input format:  
- a single line containing two integers a and b.  

output format:  
- print all lucky numbers between a and b inclusive, separated by a space, in increasing order.  
- if there are no lucky numbers, print -1.  

constraints:  
- 1 ≤ a ≤ b ≤ 10⁵  

sample input 1  
4 20  

sample output 1  
4 7  

sample input 2  
8 15  

sample output 2  
-1  """
A, B = map(int, input().split())
result = []
for num in range(A, B + 1):
    lucky = True
    for digit in str(num):
        if digit not in {'4', '7'}:
            lucky = False
            break
    if lucky:
        result.append(str(num))

print(" ".join(result) if result else "-1")