"""
# Age in Days

## Description:
Given a number N representing a person's age in days, convert it into years, months, and days.

- 1 year = 365 days
- 1 month = 30 days

## Input Format:
- The first line contains an integer T, the number of test cases.
- Each test case consists of a single integer N (the number of days).

## Output Format:
For each test case, print the age in years, months, and days in the following format:
X years  
Y months  
Z days  

## Constraints:
- 1 ≤ T ≤ 10
- 1 ≤ N ≤ 10^6

## Sample Input:
1  
400  

## Sample Output:
1 years  
1 months  
5 days  

## Sample Input 2:
2  
800  
10  

## Sample Output 2:
2 years  
2 months  
10 days  
0 years  
0 months  
10 days  
"""

# Read number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())  # Read number of days

    year = n // 365  # Calculate years
    rd = n % 365  # Remaining days after full years
    month = rd // 30  # Calculate months
    day = rd % 30  # Remaining days after full months

    # Print results
    print(year, "years")
    print(month, "months")
    print(day, "days")
