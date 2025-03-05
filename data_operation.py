"""
# Description
In Python, you can perform operations on different data types, and each operation yields a specific result.

## Task:
1. Read inputs of the following types in order:
   - An integer (int)
   - A floating-point number (float)
   - A string (str)
   - A boolean (bool)
   - A None value represented by the string "None"

2. Perform operations:
   - Add the integer and the float.
   - Concatenate the string with "Python".
   - Convert the boolean to an integer and multiply it by the float.
   - Convert the None value to a string and concatenate it with "Value".

3. Print the results, formatting all floating-point outputs to 2 decimal places.

## Input Format:
One line containing space-separated values in the order:
   - int float str bool None (represented as "None")

## Output Format:
Print the results:
   - Sum of integer and float (formatted to 2 decimal places)
   - Concatenation of string with "Python"
   - Multiplication of boolean (as int) with float (formatted to 2 decimal places)
   - Concatenation of "None" with "Value"

## Constraints:
   - −10^9 ≤ integer ≤ 10^9
   - −10^9 ≤ float ≤ 10^9
   - 1 ≤ |str| ≤ 100
   - Boolean is either True or False (case-sensitive).
   - None represents the absence of a value.
"""

a, b, c, d, e = input().split()
f = d == "True"  
x = int(a) + float(b) 
y = c + "Python"
z = int(f) * float(b) 
p = e + "Value"  
# Print results
print(f"{x:.2f}") 
print(y)
print(f"{z:.2f}")  
print(p)

