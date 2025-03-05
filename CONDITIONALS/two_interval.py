"""
# Two Intervals

## Description:
Given the boundaries of two intervals, determine the intersection of these intervals.  

- If the intervals overlap, print the boundaries of the intersection.  
- If there is no intersection, print `-1`.  

## Input Format:
- The first line contains an integer T, the number of test cases.  
- Each test case consists of four integers:  
  `l1 r1 l2 r2` representing two intervals `[l1, r1]` and `[l2, r2]`.  

## Output Format:
For each test case, print:  
- The intersection boundaries if they exist.  
- `-1` if the intervals do not overlap.  

## Constraints:
- 1 ≤ T ≤ 10^5  
- 1 ≤ l1, l2, r1, r2 ≤ 10^9  

## Sample Input:
1  
1 15 5 27  

## Sample Output:
5 15  

## Sample Input 2:
1  
3 9 5 6  

## Sample Output 2:
5 6  

## Sample Input 3:
1  
2 5 6 12  

## Sample Output 3:
-1  
"""

# Read number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    l1, r1, l2, r2 = map(int, input().split())

    # Check if intervals do not overlap
    if r2 < l1 or l2 > r1:
        print(-1)
        continue

    # Find intersection boundaries
    l = max(l1, l2)
    r = min(r1, r2)

    print(f"{l} {r}")
